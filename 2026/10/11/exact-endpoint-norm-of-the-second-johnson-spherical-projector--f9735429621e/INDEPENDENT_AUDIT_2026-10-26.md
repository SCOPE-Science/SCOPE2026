# Independent mathematical audit

## correctness

PASS

Complete analytical reconstruction: for J=|S∩T| hypergeometric with weights C(k,j)C(n−k,k−j)/C(n,k), factorial moments E(J)_r=(k)_r²/(n)_r (r≤3) imply E q=E(Jq)=0. A stabilizer-radial degree≤2 function orthogonal to the constant and degree-one slice components lies in the irreducible (n−2,2) component; Schur/trace normalization with Q(k)=d2=n(n−3)/2 fixes Q=Aq. The exact row/column endpoint norms are E|Q(J)|. Positive q at 0 and k and its negative-weight interval between real roots yield a two-tail equality even if an endpoint root is integral. Independent SymPy simplification verifies (n−1)(n−2)q(j)w_j=F(j−1)−F(j) and the exact centered quadratic formula symbolically. A separate exact-rational verifier recomputed E q=0, E Jq=0, E Q²=d2 and the exact boundary mass norm for all 961 instances n=4..64, 2≤k≤n/2, including integer roots; full independent rational spectral-polynomial projections were constructed from the Johnson adjacency for (n,k)=(4,2),(5,2),(6,2),(6,3),(7,3), and entries exactly matched Aq(|S∩T|)/C(n,k), with P²=P. For k/n→ρ∈(0,1/2], σ²=k²(n−k)²/[n²(n−1)] scales linearly, the hypergeometric CLT gives (J−μ)/σ⇒N(0,1), the linear centered term is o(n), and E(Q/n)²=d2/n²≤1/2 ensures uniform integrability; thus norm/n→(1/2)E|Z²−1|=sqrt(2/(πe)). Finite tests corroborate rather than replace the proof. Complementation reduces k>n/2 to min(k,n−k).

## originality

PASS

Best-of-knowledge PASS for the exact finite E_2 operator norm expressed by two hypergeometric boundary masses and the density-independent bulk asymptotic. The degree-two Johnson kernel, Hahn spherical function, and generic Rodrigues finite-difference formula are classical and not claimed original; the latter mechanically explains telescoping. Full primary-source comparisons of Scarabotti–Tolli, Filmus, Krebs–Shaheen, Dunkl (complete authorized 11-page paper), DLMF, Dette, and Elezović do not yield a stated equivalent endpoint norm/limit. Three published adjacent computations were read completely: degree-two Walsh and Hamming projector norms and two-coordinate Johnson face compression; none implies the finite Johnson k-slice norm. The exact matching published finding is the audited item itself and was excluded as independent priority evidence. An older Hahn Lebesgue-constant identity, an unindexed table, or a short corollary from general Hahn Rodrigues plus normalization remains an explicit risk; absence from searched sources is not proof of historical novelty.

## value

PASS

The (n−2,2) primitive idempotent is a canonical Johnson scheme spectral projector on the natural finite k-subset spaces. Its induced l1/l∞ norm measures sharp amplification of degree-two harmonic projection, unlike L2 orthogonality or eigenvalues recorded in tables. The formula computes that invariant for every admissible pair (n,k) via two exact boundary hypergeometric masses instead of an absolute sum over k+1 intersection classes; the fixed positive density limit gives the same sharp Gaussian-chaos linear-growth constant for all densities. This is a natural all-parameter exact invariant (and a usable benchmark for discrete harmonic analysis), not an arbitrary numerical slice. Its methodology is elementary from standard Hahn theory, and it makes no general higher-degree or second-order phase claim; value is limited but substantive if this specific exact norm is not prior tabulated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
