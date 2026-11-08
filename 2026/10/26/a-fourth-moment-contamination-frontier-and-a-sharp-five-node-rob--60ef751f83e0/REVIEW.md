# Independent mathematical audit

## correctness

PASS

For L>1 and 0<eps<1, the symmetric variance-mixture moments are m2=1+eps(L²-1), m4=3[1+eps(L⁴-1)]; the unique 3-node degree-five Gauss rule has P3=x³-(m4/m2)x and positive weights m2²/(2m4) at each ±sqrt(m4/m2), 1-m2²/m4 at zero. E[V²]>=E[V]² implies center weight >=2/3. If theta=eps*L⁴->c<infinity, eps*L²->0 so the displayed three-atom Gc is exact; if theta->infinity, 2w_±=m2²/m4 <= 1/(3theta)+2/(3L²)+eps/3 ->0. A subsequence argument gives G_L->G0 iff theta->0. For any positive degree-five-exact rule with <=4 nodes converging weakly to three separated G0 atoms, at least three nodes remain in bounded neighborhoods; at most one additional node can escape. Because the fifth moment is exactly zero, its positive weighted term v*z^5 is minus a bounded core contribution, whence v*z^4=o(1), incompatible with m4->infinity. The explicit five-node rule has total mass 1, correct m2,m4 and zero odd moments through 5, with escaping pair mass eps/3->0. For eps=L^-3, bounded witness e^-x² gives limits 1 versus 1/sqrt(3). Independently verified 48 rational mixtures, positivity, moment identities, 5-node attainment, three asymptotic scales and bounded witness. Finite checks supplement unrestricted proofs; not proof of general moment-map stability under arbitrary contaminations.

## originality

PASS

Best-of-knowledge assessment: the joint theorem of sharp epsilon*L^4 weak-limit phases, positive four-node impossibility and five-node attainment is not covered by the actual statements inspected in classical moment-based Gaussian quadrature, Kabaila 2026, Shim 2026 abstract, Pinkse 2026, Xu 1994, Trefethen 2021 or the published Resultary moment/Hermite findings. The cubic and componentwise construction by themselves are classical. The 4-node lower bound is genuinely stronger than standard quadrature formulas; unindexed older exact-equivalent results remain possible.

## value

PASS

The two-component centered Gaussian variance mixture is a natural stress test for positive moment-fitted numerical integration under vanishing total-variation contamination. The epsilon*L⁴ threshold is sharp and mathematically interpretable as the uncontrolled fourth moment; the bounded smooth witness shows genuine loss of distributional fidelity. The exact positive node budget (3 fails and every 4-node rule fails, while 5 works) identifies a meaningful algorithmic design tradeoff without claiming universal quadrature accuracy. This is a structural theorem with a motivated optimal finite cutoff, not merely the classical 3-node Hermite formula or an arbitrary table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
