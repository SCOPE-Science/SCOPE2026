# One-site Rule 150 defects and a dyadic first-entry law on Rule 90 rings

## Finding
For each integer \(n\ge3\), consider a labelled cyclic ring with binary states and synchronous updates
\[
(F_n(x))_i=x_{i-1}\oplus x_{i+1}\oplus\mathbf1_{\{i=0\}}x_0,
\qquad i\in\mathbb Z/n\mathbb Z,
\]
where \(\oplus\) denotes addition in \(\mathbb F_2\). Every site except the distinguished site \(0\) uses Rule 90; site \(0\) uses Rule 150. For an initial configuration \(x\), let \(T(x)\) be the least nonnegative integer such that \(F_n^{T(x)}(x)\) is periodic.

Set \(s=\nu_2(n)\) and \(q=2^s-1\). Then, **for every** \(n\ge3\),
\[
\#\{x:T(x)=0\}=2^{n-q},\qquad
\#\{x:T(x)=t\}=2^{n-q+t-1}\quad(1\le t\le q),
\]
with no other possible values of \(T\). In particular, \(F_n\) is bijective exactly for odd \(n\). For even \(n\), the proportion of initially periodic configurations is \(2^{-q}\), the exact maximum first-entry time is \(q\), and a uniformly random initial configuration satisfies
\[
\Pr(T=t)=2^{t-1-q}\quad(1\le t\le q),\qquad
\mathbb ET=q-1+2^{-q}.
\]
For odd \(n\), all configurations are initially periodic, so \(T=0\) identically.

There is also a precise comparison with the **unmodified**, uniform Rule 90 map on the same ring. For odd \(n\), uniform Rule 90 has a one-dimensional nilpotent component and is never bijective, whereas the single defect makes every configuration periodic. For even \(n\) with \(s\ge1\), uniform Rule 90 has two nilpotent Jordan blocks, each of size \(2^{s-1}\), while the one-site defect has **one** nilpotent Jordan block of size \(2^s-1\). Thus the defect doubles the initially periodic population, but for \(s\ge2\) raises the sharp maximal transient length from \(2^{s-1}\) to \(2^s-1\). This comparison is part of the same result, not a separate claim.

## Assumptions and scope
The state space is \(\mathbb F_2^n\), the vertices are fixed and labelled, and the update is simultaneous. Only site \(0\) differs from the usual two-neighbor XOR rule, by adding its **own** previous state. A temporal periodic point means \(F_n^p(x)=x\) for some integer \(p\ge1\); spatial rotations are not identified. The rings have \(n\ge3\), so both immediate neighbors are distinct. The parity valuation is \(\nu_2(n)=0\) for odd \(n\).

## Proof
**1. Characteristic polynomial.** Let \(W_n\) be the adjacency matrix of the \(n\)-cycle over \(\mathbb F_2\), and \(E_{00}\) the matrix with a single \(1\) at position \((0,0)\). Then \(F_n\) is represented by \(B_n=W_n+E_{00}\). Let \(p_k(z)\) be the characteristic polynomial over \(\mathbb F_2\) of the \(k\)-vertex path adjacency matrix, so
\[
p_0(z)=1,\qquad p_1(z)=z,\qquad
p_k(z)=z p_{k-1}(z)+p_{k-2}(z)\quad(k\ge2).
\]
The cycle determinant identity \(\det(zI-W_n)=z p_{n-1}(z)\) follows by expanding the two wrap-around contributions, which cancel in characteristic two; it is also the published path/cycle identity of Lettieri–Stevens–Thomas [2, Theorem 3.1]. Changing a single diagonal entry changes the determinant by the complementary principal minor, equal to \(p_{n-1}(z)\). Hence
\[
\boxed{\chi_{B_n}(z)=(z+1)p_{n-1}(z).}
\]

**2. Exact multiplicity of the zero eigenvalue.** Write \(n=2^s m\) with \(m\) odd. In an algebraic extension of \(\mathbb F_2(z)\), let \(\alpha,\beta\) be the roots of \(u^2+zu+1=0\); then \(\alpha+\beta=z\), and the path recurrence gives
\[
p_{k-1}(z)=\frac{\alpha^k+\beta^k}{z}.
\]
Frobenius therefore yields the polynomial identity
\[
\boxed{p_{n-1}(z)=z^{2^s-1}p_{m-1}(z)^{2^s}.}
\]
Because \(m-1\) is even, \(p_{m-1}(0)=1\). Thus the zero eigenvalue of \(B_n\) has algebraic multiplicity exactly \(q=2^s-1\). For odd \(n\), \(q=0\), so \(B_n\) is invertible.

**3. One zero Jordan chain when \(n\) is even.** The equations \(B_nx=0\) away from site \(0\) are \(x_{i-1}=x_{i+1}\). For odd \(n\), these force every coordinate equal, and the equation at site \(0\) then forces all coordinates zero. For even \(n\), they force a common value on each of the even and odd vertex classes; the equation at site \(0\) kills the even-class value but leaves the odd-class value free. Hence \(\dim\ker B_n=1\) for even \(n\). The number of Jordan blocks at the zero eigenvalue equals this nullity, so its whole generalized zero eigenspace consists of one nilpotent Jordan block of length \(q\).

**4. First-entry populations.** The Fitting decomposition is the direct sum of a \(q\)-dimensional nilpotent block and an \((n-q)\)-dimensional invertible component. Over the finite field, every vector in the invertible component is periodic, and the zero-component vector is the only periodic vector in the nilpotent block. Consequently
\[
\#\{x:T(x)\le t\}=2^{n-q+\min(t,q)}\quad(t\ge0).
\]
Taking successive differences proves the exact populations. The maximum \(q\) is attained because the length-\(q\) Jordan chain has vectors not killed by the preceding power. The expectation follows from summing the finite geometric-weighted series.

**5. Uniform-rule comparison.** Over \(R=\mathbb F_2[u]/(u^n-1)\), uniform Rule 90 is multiplication by \(u+u^{-1}=u^{-1}(u+1)^2\). The factor \((u+1)^{2^s}\) in \(u^n-1=(u^m+1)^{2^s}\) describes the entire generalized zero eigenspace. For \(s\ge1\), multiplication by \((u+1)^2\) on the local ring \(\mathbb F_2[v]/(v^{2^s})\) has exactly two Jordan chains, each of length \(2^{s-1}\), while all other primary factors are invertible. For \(s=0\), there is one one-dimensional zero block. The stated transient-horizon and periodic-population comparisons follow immediately.

## Verification
The attached standalone script `verify.py` checks all binary matrix-power ranks for both updates for each size from \(3\) through \(80\), against the ranks predicted by the Jordan decompositions. It independently traces all \(4{,}088\) labelled initial configurations of sizes \(3\) through \(11\) until their first repeat, classifying exact preperiod lengths. With SymPy available it also evaluates the characteristic polynomial by direct matrix calculation at every size from \(3\) through \(17\), independent of the symbolic argument above. The attached `verification_output.txt` records all passing checks; these finite calculations corroborate but do not replace the all-size proof.

For example, at \(n=4\) the first-entry shell counts are \((2,2,4,8)\) for times \(0,1,2,3\); at \(n=6\) they are \((32,32)\); at \(n=8\) they are \((2,2,4,8,16,32,64,128)\).

## Relationship to prior work
Martin–Odlyzko–Wolfram [1] and Lettieri–Stevens–Thomas [2] analyze the uniform finite Rule 90 system; specifically, [2, Theorem 3.1] gives the cycle/path characteristic-polynomial identity used here. Dennunzio–Formenti–Provillard [3] establishes a general framework for non-uniform cellular automata and motivations for finite local perturbations, but studies broader qualitative properties on bi-infinite lattices rather than this precise finite-ring first-entry census. Katona [4] analyzes finite inhomogeneous automata, but its special notion of reversibility requires an inverse with the same local-neighborhood structure, rather than only the global bijectivity addressed here. This distinction avoids an erroneous contradiction with [4].

The novelty assessed here is specifically the one-site Rule 150 perturbation and the exact valuation-dependent Jordan block and all first-entry shell populations, including the comparison with uniform Rule 90; no novelty is claimed for the known uniform-rule characteristic polynomial or general Fitting/Jordan machinery.

## Limitations
The result does not enumerate primitive **period lengths** inside the invertible component, nor quantify sensitivity to multiple modified sites or to noise. It concerns finite, labelled, synchronous rings only, and does not assert a translation-equivariant inverse on the bi-infinite line. Existing work on hybrid rules and on linear automata with boundary conditions could contain equivalent special cases that were not accessible in full. This is a self-review mathematical argument with finite computational corroboration, not independently audited or machine-certified mathematics.

## References
[1] O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: `10.1007/BF01223745`. Full author-uploaded text: https://www.researchgate.net/publication/38329520_Algebraic_Properties_of_Cellular_Automata.

[2] S. Lettieri, J. G. Stevens, D. M. Thomas, *Characteristic and Minimal Polynomials of Linear Cellular Automata*, Rocky Mountain Journal of Mathematics **36** (2006), 1077–1092. DOI: `10.1216/rmjm/1181069447`. Author-uploaded full text: https://www.researchgate.net/publication/38371117_Characteristic_and_Minimal_Polynomials_of_Linear_Cellular_Automata.

[3] A. Dennunzio, E. Formenti, J. Provillard, *Non-Uniform Cellular Automata: Classes, Dynamics, and Decidability*. arXiv `1107.5228v1`, publicly posted **2011-07-26**: https://arxiv.org/abs/1107.5228.

[4] E. Katona, *Local and Global Reversibility of Finite Inhomogeneous Cellular Automaton*, Acta Cybernetica **3** (1977), 287–292. Open full text: https://acta.bibl.u-szeged.hu/12254/1/cybernetica_003_fasc_004_287-292.pdf.

[5] W. Chin, B. Cortzen, J. Goldman, *Linear Cellular Automata with Boundary Conditions*, Linear Algebra and its Applications **322** (2001), 193–206. DOI: `10.1016/S0024-3795(00)00227-5`. Full text not accessed; considered as a residual equivalence risk.
