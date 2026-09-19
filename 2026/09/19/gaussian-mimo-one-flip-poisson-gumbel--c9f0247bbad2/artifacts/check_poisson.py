import math
import numpy as np

# Monte Carlo sanity check for the one-bit count law.
# The reduced simulation uses rotational invariance: conditional on ||w||=r,
# h^T w = r g and ||h||^2 = g^2 + Z with g~N(0,1), Z~chi^2_{m-1}.

rng = np.random.default_rng(20260919)
lambda0 = 1.0 / (2.0 * math.sqrt(math.pi))

for N, alpha, trials in [(400, 1.0, 4000), (800, 1.0, 3000), (600, 1.5, 3000)]:
    m = int(round(alpha * N))
    alpha_exact = m / N
    tau = 2.0 * math.log(N) - math.log(math.log(N))
    rho = tau / alpha_exact
    s = math.sqrt(rho / N)
    counts = []
    batch = 100
    for start in range(0, trials, batch):
        b = min(batch, trials - start)
        r = np.sqrt(rng.chisquare(m, size=(b, 1)))
        g = rng.standard_normal((b, N))
        z2 = rng.chisquare(m - 1, size=(b, N))
        norm2 = g * g + z2
        counts.append((r * g + s * norm2 < 0.0).sum(axis=1))
    K = np.concatenate(counts)
    print(
        f"N={N} alpha={alpha:g} mean={K.mean():.6f} "
        f"p0={(K == 0).mean():.6f}"
    )

print(f"limit_mean={lambda0:.6f} limit_p0={math.exp(-lambda0):.6f}")
