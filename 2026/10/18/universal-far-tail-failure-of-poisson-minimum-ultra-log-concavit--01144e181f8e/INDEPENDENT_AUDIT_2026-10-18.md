# Independent mathematical audit

## correctness

PASS

Conditioning on N=n gives r_k=p_k H_k with H_k=w_1+w_2(S_k+S_{k+1})+R_k where survival S_k=P(X>=k), p_k=S_k-S_{k+1}. For S_k<=1/2, every n>=3 remainder contribution obeys n S_k^{n-1}<=3 S_k^2, uniformly over all N laws even E[N]=infinite. Poisson tail S_k/p_k→1, S_{k+1}/p_k→0, and p_k/p_{k-1}→0 imply H_{k-1}H_{k+1}-H_k² = w_1w_2 p_{k-1}(1+o(1)). Exact Poisson three-term ratio is k/(k+1), yielding stated positive curvature. N=1 is Poisson ULC equality; N=2 factor (S_k+S_{k+1}) is log-concave by convolution of two log-concave sequences, giving deterministic ULC. Positive mixtures excluded by asymptotic. Independent finite mpmath evaluations at lambda=2.1/w1=.57 show normalized tail/asymptotic ratios approach 1 (e.g. k=12: 0.972, k=30:0.995). Numerics only corroborate analytic proof.

## originality

PASS

Badiella–del Castillo–Puig fixed-N discrete-order-statistic ULC preservation does not imply closure under mixing over N; the claim shows the opposite, with an explicit universal far-tail asymptotic even for unbounded N. The complete original paper could not be materially read due OA gateway denial and authorized Oxford VPN disconnected; this is an explicit coverage risk rather than automatic O failure.

## value

PASS

A sharp and robust non-closure theorem for an established discrete shape constraint: any positive mixing of just sample sizes one and two eventually reverses ULC despite each fixed-size minimum retaining it. The leading defect uses only the first two size masses even when higher-size mass has infinite mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
