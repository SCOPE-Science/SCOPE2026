# Alternating-cycle spectra and sharp noncommutativity of matching-coarse-grained Parseval frames

## Finding

For each even integer \(n=2m\ge4\), place the standard centered simplex vertices in \(V=\mathbf1^\perp\subset\mathbb C^n\). The centered edge vectors
\[
v_{\{i,j\}}=\frac{e_i+e_j-(2/n)\mathbf1}{\sqrt{n-2}},\qquad 1\le i<j\le n,
\]
form a Parseval frame. For each perfect matching \(M\) of the complete graph on \(n\) vertices, define its binary coarse-grained effect \(E_M=\sum_{e\in M}v_ev_e^*\).

Superpose two perfect matchings \(M,N\) as a two-colored multigraph, keeping a shared edge twice. Its connected components are alternating cycles of lengths \(2k_1,\dots,2k_s\), with a doubled shared edge regarded as length two (\(k_a=1\)). The complete complex eigenvalue multiset of the commutator is
\[
\operatorname{Spec}([E_M,E_N])=
\left(\biguplus_{a=1}^s\biguplus_{j=0}^{k_a-1}
\left\{\frac{2i\sin(2\pi j/k_a)}{(n-2)^2},
\frac{2i\sin(2\pi j/k_a)}{(n-2)^2}\right\}\right)\setminus\{0\},
\]
where one zero is removed with its multiplicity, corresponding to the constant direction omitted from \(V\). In particular,
\[
\|[E_M,E_N]\|=\frac{2}{(n-2)^2}\max_{a,j}|\sin(2\pi j/k_a)|.
\]
They commute if and only if every component is a doubled edge or alternating four-cycle.

The sharp maximum over all \(M,N\) is zero for \(n=4\), is \(\sqrt3/16\) for \(n=6\), and equals \(2/(n-2)^2\) for every even \(n\ge8\). At \(n=6\) precisely alternating six-cycles attain the maximum. For even \(n\ge8\), equality holds exactly when at least one alternating component has length divisible by eight.

For any fixed \(M\), the exact number of commuting perfect matchings \(N\) is
\[
C_m=\sum_{t=0}^{\lfloor m/2\rfloor}\frac{m!}{(m-2t)!\,t!}.
\]
The exact number of maximizing partners for \(m\ge4\) is the integer
\[
A_m=m!\,[z^m]\frac{1-(1-16z^4)^{1/8}}{\sqrt{1-2z}}.
\]
Here \([z^m]\) extracts a formal power-series coefficient, so no analytic branch choice is involved.

The binary POVMs \((E_M,I-E_M)\) and \((E_N,I-E_N)\) are jointly measurable for every pair, including those attaining the largest commutator norm. This exhibits a fully quantified compatibility-versus-commutativity gap.

## Assumptions and scope

All spaces are complex Hilbert spaces with the standard inner product; the frame vectors are real. The integer \(n\) is even and at least four. Each \(M,N\) is a perfect matching of \(K_n\). The commutator is \([A,B]=AB-BA\); norms are Hilbert operator norms. The spectrum includes algebraic multiplicities, with the convention for doubled shared edges stated above. No claim is made for arbitrary subsets of edges, weighted frame vectors, or nonmatching partitions.

## Proof

**1. Parseval normalization.** Set \(p_i=e_i-\mathbf1/n\) and \(P_V=I-\mathbf1\mathbf1^*/n\). Then \(\sum_i p_i=0\) and \(\sum_i p_ip_i^*=P_V\). Expanding the edge sums gives
\[
\sum_{i<j}(p_i+p_j)(p_i+p_j)^*
=(n-2)\sum_i p_ip_i^*+\Bigl(\sum_i p_i\Bigr)\Bigl(\sum_i p_i\Bigr)^*
=(n-2)P_V.
\]
Division by \(n-2\) proves the Parseval property.

**2. Matching compression identity.** Let \(R_M\) be the real permutation matrix interchanging the vertices of every matched pair in \(M\); it is a selfadjoint involution and fixes \(\mathbf1\). The uncentered matched-edge sum is
\[
\sum_{\{i,j\}\in M}(e_i+e_j)(e_i+e_j)^*=I+R_M.
\]
Consequently, on \(\mathbb C^n\) with the effect extended by zero on \(\mathbb C\mathbf1\),
\[
E_M=\frac{I+R_M-2\mathbf1\mathbf1^*/n}{n-2}
=\frac2{n-2}P_M,
\qquad P_M=\frac{I+R_M}2-\frac{\mathbf1\mathbf1^*}n.
\]
Here \(P_M\) is the orthogonal projector onto the mean-zero vectors constant on each matched pair. Since every \(R_M\) commutes with \(\mathbf1\mathbf1^*\),
\[
[E_M,E_N]=\frac{R_MR_N-R_NR_M}{(n-2)^2}.
\]

**3. Full spectrum from alternating cycles.** The permutation \(W=R_MR_N\) is unitary, with \(W^*=R_NR_M=W^{-1}\). On a component consisting of \(2k\) vertices, \(W\) permutes each color class of alternating vertices in a \(k\)-cycle. Thus the \(k\)th roots of unity occur twice each on that component (including \(k=1\)). Since \([E_M,E_N]=(W-W^*)/(n-2)^2\), its eigenvalues on this component are \(2i\sin(2\pi j/k)/(n-2)^2\), twice for each \(0\le j<k\). Every component contributes a zero mode; deleting the global constant vector removes exactly one zero. This proves the claimed multiset and norm formula.

**4. Commuting and sharp-extremal cycles.** The sine values vanish for all integer \(j\) exactly when \(k=1\) or \(2\). They have absolute value one for some integer \(j\) exactly when \(4\mid k\). At \(n=4\) all \(k\le2\). At \(n=6\) the only nonzero case has \(k=3\), whose largest sine modulus is \(\sqrt3/2\). For \(n\ge8\), choose an alternating eight-cycle (\(k=4\)) and leave all remaining matched pairs unchanged. This attains \(2/(n-2)^2\). These facts also prove every equality characterization.

**5. Counts.** Fix \(M\) with \(m\) edges. For a commuting \(N\), select \(2t\) of the \(m\) matched pairs, pair them into \(t\) two-block groups, and in each group choose one of two cross reconnections. Hence
\[
\binom m{2t}\frac{(2t)!}{2^t t!}\,2^t
=\frac{m!}{(m-2t)!t!}
\]
choices, and summing over \(t\) gives \(C_m\). More generally, for a selected collection of \(k\) original matching edges, the number of ways to join them into a single alternating \(2k\)-cycle is \(2^{k-1}(k-1)!\), including the shared-edge case \(k=1\). The labelled assembly exponential generating function for all partner matchings is
\[
\exp\!\left(\sum_{k\ge1}\frac{2^{k-1}}k z^k\right)=(1-2z)^{-1/2}.
\]
To exclude every cycle with \(4\mid k\), remove the corresponding summands in its exponent. The resulting series is
\[
(1-2z)^{-1/2}\exp\!\left(-\sum_{\ell\ge1}\frac{2^{4\ell-1}}{4\ell}z^{4\ell}\right)
=(1-2z)^{-1/2}(1-16z^4)^{1/8}.
\]
Subtracting its coefficient from the coefficient counting all \((2m-1)!!\) partners gives \(A_m\).

**6. Joint measurement.** The four positive operators
\[
F_{ab}=\sum_{e:\,\mathbf1_{M}(e)=a,\,\mathbf1_{N}(e)=b}v_ev_e^*,
\qquad a,b\in\{0,1\},
\]
partition the full Parseval frame and sum to the identity on \(V\). Their respective two-outcome marginals are \((E_M,I-E_M)\) and \((E_N,I-E_N)\). This explicitly proves joint measurability, without requiring their effects to commute.

## Verification

Run the standalone checker `verify_matching_effects.py` using Python 3 and NumPy. It checks the Parseval and matching identities and all spectra for every partner matching relative to a fixed base matching at \(n=4,6,8,10\). Since simultaneous relabeling acts transitively on base matchings, this exhausts all pairs up to relabeling at those sizes. For \(n=12\), it exhaustively checks the exact integer commutator identity and commuting/maximizing classifications, without using numerical eigensolvers. The run printed `VERIFICATION_OK`; it found respective commuting-partner counts \(3,7,25,81,331\) and maximizing-partner counts \(0,0,48,240,2160\) at \(n=4,6,8,10,12\). Finite tests corroborate, but do not prove, the arbitrary-dimensional theorem.

## Relationship to prior work

Kużel and Łukasiewicz establish the common-Parseval-frame construction of jointly measurable POVMs and investigate spectra of single frame-generated operators, including Mercedes-type and conference-matrix frames. Their Proposition 3.4 provides the general joint-measurability context, not a commutator spectrum for pairs of matching-selected effects. Deregowska and Lewandowska study an edge-midpoint configuration for projection constants; their full finite family also includes additional indexed vectors and is not identical to the present off-diagonal edge-only Parseval frame. Their projection-constant formulas do not determine the present commutators. Halmos's two-projection theorem controls arbitrary pairs of orthogonal projections abstractly; evaluating the matching-specific permutation product, complete equality cycles, and the enumeration of partners is the additional content here. A prior matching-deletion calculation for the same edge-only frame concerns renormalized Gram projections and their \(\ell_\infty\) norms, not pairwise commutator spectra or partner counts. A separate Mercedes-frame coarse-graining calculation involves a different Gram projection and does not imply the alternating-cycle law.

## Limitations

The result is exact only for perfect-matching coarse-grainings of the specific centered edge-only Parseval frame, with even vertex number. No general frame-uniform noncommutativity bound, state-dependent incompatibility measurement, or claim about arbitrary two-valued partitions is inferred. The spectral proof uses classical theory of two projections and elementary permutation-cycle eigenvalues; a historical result expressing this specialized calculation in another terminology could affect publication priority. Independent external mathematical review has not been performed.

## References

1. S. Kużel and P. Łukasiewicz, *Operators and POVMs generated by Parseval frames*, arXiv:2601.11225 (first version 2026-01-16); *Banach Journal of Mathematical Analysis* 20, article 49 (2026), DOI 10.1007/s43037-026-00514-0.
2. B. Deregowska and B. Lewandowska, *Maximal Projection Constants and Extremal Vector Configurations: Some Conjectures and Examples*, arXiv:2608.08695 (first version 2026-08-09), especially Example 2.1.
3. P. R. Halmos, *Two subspaces*, *Transactions of the American Mathematical Society* 144 (1969), 381–389, DOI 10.1090/S0002-9947-1969-0251519-5.
