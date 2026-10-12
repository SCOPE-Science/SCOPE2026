from decimal import Decimal, getcontext
getcontext().prec = 80
E = Decimal(1).exp()

def exp(x):
    return Decimal(x).exp()

# All huge exponentials are divided by their natural common scale.
# 1) Heavy-prime / final-smooth slack:
#    3073*(e^-3200/5) < e^-1400/2
heavy_ratio = (Decimal(3073)/Decimal(5)) * exp(-1800)
heavy_margin = Decimal(1)/2 - heavy_ratio
assert heavy_margin > 0

# 2) Small-prime richness, using 1/N <= e^-200000:
#    e^-200000 + 2*(e^-3200/5) < e^-3200/2.
pair_ratio = exp(-196800) + Decimal(2)/Decimal(5)
pair_margin = Decimal(1)/2 - pair_ratio
assert pair_margin > 0

# 3) Coupling failure term 8*delta/c0 < 1/8.
coupling_ratio = (Decimal(8)/Decimal(5)) * exp(-1800)
coupling_margin = Decimal(1)/Decimal(8) - coupling_ratio
assert coupling_margin > 0

# Improvement factor over the published e^-5000.
# (e^-3200/5) / e^-5000 = e^1800/5.
log_improvement = Decimal(1800) - Decimal(5).ln()
assert log_improvement > Decimal(1798)

# A few stronger sanity inequalities used in the written proof.
assert exp(-196800) < Decimal(1)/10
assert heavy_ratio < Decimal(1)/2
assert coupling_ratio < Decimal(1)/8

print('VERIFY_OK',
      'heavy_margin_scaled=' + format(heavy_margin, '.25E'),
      'pair_margin_scaled=' + format(pair_margin, '.25E'),
      'coupling_margin=' + format(coupling_margin, '.25E'),
      'log_improvement=' + format(log_improvement, '.25f'))
