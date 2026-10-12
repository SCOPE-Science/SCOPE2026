from mpmath import mp

mp.dps = 80


def log_exact_tail(alpha, y):
    a = mp.mpf(alpha)
    yy = mp.mpf(y)
    r = 1 / a
    log_m = mp.loggamma(r + 1)
    log_q = mp.loggamma(2 * r + 1)
    delta = mp.e ** (2 * log_m - log_q)
    log_s = mp.mpf('0.5') * log_q + mp.mpf('0.5') * mp.log1p(-delta)
    log_threshold = log_s + mp.log(yy) + mp.log1p(mp.e ** (log_m - log_s) / yy)
    exponent = mp.e ** (a * log_threshold)
    return -exponent, log_m - log_s


def log_profile_asymptotic(alpha, y):
    a = mp.mpf(alpha)
    yy = mp.mpf(y)
    return (
        -2 / (mp.e * a)
        + mp.log(a) / (2 * mp.e)
        - mp.log(4 * mp.pi) / (2 * mp.e)
        - (2 / mp.e) * mp.log(yy)
    )


alphas = [mp.mpf(x) for x in ('0.1', '0.05', '0.025', '0.0125', '0.00625')]
ys = [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2')]
errors = []
terminal_errors = []
for y in ys:
    local = []
    for a in alphas:
        lex, log_ms = log_exact_tail(a, y)
        las = log_profile_asymptotic(a, y)
        local.append(abs(lex - las))
        assert log_ms < 0
    errors.extend(local)
    terminal_errors.append(local[-1])
    assert local[-1] < local[0]

# The limiting threshold-ratio law follows from the same profile.
a = mp.mpf('0.00625')
l1, _ = log_exact_tail(a, mp.mpf('0.5'))
l2, _ = log_exact_tail(a, mp.mpf('2'))
observed = mp.e ** (l1 - l2)
predicted = (mp.mpf('2') / mp.mpf('0.5')) ** (2 / mp.e)
assert abs(observed / predicted - 1) < mp.mpf('0.02')
assert max(terminal_errors) < mp.mpf('0.02')

print(
    'VERIFY_OK '
    f'alpha_min={mp.nstr(alphas[-1], 8)} '
    f'max_terminal_log_error={mp.nstr(max(terminal_errors), 12)} '
    f'ratio_rel_error={mp.nstr(abs(observed / predicted - 1), 12)}'
)
