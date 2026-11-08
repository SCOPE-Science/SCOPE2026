# Independent mathematical audit

## correctness

PASS

Independently reconstructed five transitive C2×C2 orbit types, sizes 1,2,2,2,4: each contributes z^d/d, giving F(z)=exp(z+3z²/2+z⁴/4). The independent Poisson sampler conditioned on total size n is exactly uniform. For saddle r>0 solving r+3r²+r⁴=n, variance V=r+6r²+4r⁴. Fourier inversion has a unique unsuppressed peak for total size (t=π suppressed by e^-2r and t=±π/2 by e^-3r²) and two peaks for the even-support sum excluding singleton type. Hence P(S=n)~1/sqrt(2πV) and P(N1=0|S=n)=0 for odd n, ~2e^-r for even n. Union bounding Poisson lower tails divided by P(S=n) gives O_q(sqrt(n)r^(q-1)e^-r) for some type count <q. A q-round EF orbit-by-orbit strategy in the total-unary-functions signature yields the uniform rank-q zero-one law. Each orbit type T has a quantifier-free unary identifier and the rank-q formula requiring q pairwise-disjoint T orbits, proving 11q minimality. Independent complete permutation enumeration n<=7 and direct polynomial convolution match OEIS, and high precision ratio at n=1600 is 0.99540962878. Finite numerics do not prove the local limits. Computed Git tree SHA from seven actual blob identities matches f28464bda051eb5dd1bf4f7e707e6bff02cefab9.

## originality

PASS

Best-of-knowledge originality applies only to the combined effective fixed-rank law with sharp 11q minimum and parity-corrected 2 exp(-r_n) rare-event term. The exact EGF/enumeration was published at least by OEIS A362819 in 2023 and must not be claimed new. Available primary results are different conditioning/models or weaker conclusions; an unseen general finite G-action theorem remains a priority risk.

## value

PASS

Conditioning two natural random involutions to commute yields a random action with five finite orbit types and qualitative behavior sharply different from unconstrained involutions. The minimum 11q size of a finite rank-q representative, the simultaneous explicit logical error bound, and the parity-corrected probability for absence of a common fixed point are interpretable structural/probabilistic facts that a researcher studying random finite group actions can use. Does not require a new general method; the already known EGF alone would not support value or originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
