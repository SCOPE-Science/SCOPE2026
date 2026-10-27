# Cyclotomic collapse and the exact dynamical phase diagram of periodically weighted shifts

## Finding
Fix an integer \(q\ge2\), a primitive \(q\)-th root of unity \(\zeta\), an arbitrary \(a\in\mathbb C\), and a nonzero complex \(q\)-periodic weight sequence \((w_k)_{k\ge1}\). For every \(1\le p<\infty\), set
\[
(Tx)_k=a\zeta^{k-1}x_k+w_kx_{k+1},\quad
W=\prod_{j=1}^{q}w_j,\quad R=|W|,\quad c=|a|^q,\quad L=|1-c|,\quad U=1+c.
\]
Then all the following statements hold simultaneously.

1. **Power collapse and similarity:** \(T^q=a^q I+B_w^q\), and the latter is isometrically conjugate to \(\bigoplus_{r=1}^q(a^qI+WB)\), where \(B\) is the unweighted unilateral backward shift. For fixed \(q,\zeta,a,p\), two such operators are similar by a bounded invertible diagonal operator if and only if their weight-product moduli \(R\) coincide. Hence the complete similarity classification within this family has one positive real invariant.
2. **Exact spectral lemniscates:**
\[
\sigma(T)=\{\lambda\in\mathbb C:|\lambda^q-a^q|\le R\},\qquad
\sigma_{\mathrm p}(T)=\{\lambda\in\mathbb C:|\lambda^q-a^q|<R\}.
\]
3. **Exact linear dynamics:** Hypercyclicity, topological mixing, frequent hypercyclicity, and Devaney chaos are equivalent for this family and occur precisely when \(R>L\).
4. **Exact shadowing threshold:** The forward shadowing property holds precisely when \(R<L\) or \(R>U\). Both equality boundaries fail shadowing.

In particular, the intervals \(R<L\), \(R=L\), \(L<R\le U\), and \(R>U\) are respectively: shadowing but not hypercyclic; neither; mixing, frequent hypercyclic and chaotic but not shadowing; and all of mixing, frequent hypercyclicity, chaos, and shadowing. The interval \(L<R\le U\) may collapse to a point or be empty (for \(a=0\), \(L=U=1\)). At \(a=1\), *every* nonzero periodic weight tuple gives mixing, frequent hypercyclicity, and chaos, while shadowing holds exactly when \(R>2\).

## Assumptions and scope
We work on the complex Banach sequence space \(\ell^p(\mathbb N)\) for any \(1\le p<\infty\). Indices begin at \(1\). The periodic weights are nonzero, not necessarily equal in magnitude or phase; no smallness, positivity, or monotonicity assumption is made. The root \(\zeta\) must have **exact order \(q\)**. The operator \(B_w\) is defined by \((B_wx)_k=w_kx_{k+1}\). The definitions of hypercyclicity, frequent hypercyclicity, mixing, Devaney chaos and forward shadowing use the usual norm topology of \(\ell^p\). The similarity assertion compares operators with the same fixed \(q,\zeta,a,p\).

## Proof
**Cyclotomic power identity.** Write \(T=D+B_w\), where \((Dx)_k=a\zeta^{k-1}x_k\). Directly on coordinates, \(DB_w=\zeta^{-1}B_wD\), with \(\zeta\) primitive. The Gaussian binomial identity at a primitive \(q\)-th root implies that every nontrivial mixed coefficient in \((D+B_w)^q\) vanishes: for \(1\le j<q\), its numerator contains \(1-\zeta^q=0\) while its denominator contains no zero factor. Thus \(T^q=D^q+B_w^q=a^qI+B_w^q\). Periodicity yields \(\prod_{h=0}^{q-1}w_{k+h}=W\) for every \(k\), hence \((B_w^qx)_k=Wx_{k+q}\). Rearrangement by residues modulo \(q\) is an isometry from \(\ell^p\) onto \(\bigoplus_{r=1}^q\ell^p\) with the \(\ell^p\)-direct-sum norm; it converts \(B_w^q\) to \(q\) copies of \(WB\).

**Spectral sets.** Since \(\sigma(B)=\overline{\mathbb D}\), spectral mapping gives \(\sigma(T^q)=a^q+W\overline{\mathbb D}\). If \(\lambda\in\sigma(T)\), then \(|\lambda^q-a^q|\le R\). Conversely, the eigenvalue recurrence
\[
x_{k+1}=\frac{\lambda-a\zeta^{k-1}}{w_k}x_k,
\qquad x_{k+q}=\frac{\lambda^q-a^q}{W}x_k
\]
has a nonzero \(\ell^p\) solution precisely for \(|\lambda^q-a^q|<R\): after each block of \(q\) coordinates the amplitudes form a geometric progression of modulus strictly below one. When that modulus is one the nonzero progression cannot be \(p\)-summable. The closed set \(\{|\lambda^q-a^q|\le R\}\) is the closure of its strict interior (\(R>0\)), proving the full spectrum inclusion in the reverse direction.

**Similarity rigidity.** Suppose \(w_k'\) is a second nonzero \(q\)-periodic tuple and \(|W'|=|W|\). Define \(s_1=1\) and \(s_{k+1}/s_k=w_k'/w_k\). Then \(s_{k+q}=(W'/W)s_k\), whose modulus equals \(|s_k|\), so the diagonal \(S=\operatorname{diag}(s_k)\) is bounded and boundedly invertible. One has \(S^{-1}T_wS=T_{w'}\). Conversely, similarity forces equal spectra; their lemniscates are strictly nested when their radii \(R\) differ, so the radii must agree.

**Sufficiency of the dynamical threshold.** Set \(A=a^qI+WB\). If \(R>L\), the disk \(\{\mu:|\mu-a^q|<R\}\) intersects the unit circle in a nonempty relatively open arc. This disk meets both the regions \(|\mu|<1\) and \(|\mu|>1\) in open sets (for the latter, an interior neighborhood of its outermost point). For each \(|z|<1\), \(v(z)=(1,z,z^2,\ldots)\in\ell^p\) and \(Av(z)=(a^q+Wz)v(z)\). The vectors with \(z\) in *any nonempty open subset* of the unit disk span densely: a continuous linear functional annihilating them yields an analytic function \(\sum_{k\ge0}h_kz^k\) that vanishes on an open set, hence all coefficient functionals vanish. This holds separately for each of the \(q\) direct-sum coordinates. Consequently, the eigenvectors of \(A^{\oplus q}=T^q\) inside and outside the unit circle each span a dense subspace; the classical Godefroy–Shapiro eigenvector criterion makes \(T^q\) topologically mixing.

For frequent hypercyclicity, choose normalized arclength measure on a closed subarc lying strictly inside the open eigenvalue arc on the unit circle. Removing any measure-zero subset still leaves infinitely many points accumulating in that arc. The same analytic argument proves that the unimodular eigenspaces of \(T^q\) are **perfectly spanning** in the sense of Grivaux. Grivaux's theorem therefore makes \(T^q\) frequently hypercyclic. The positive lower density of returns at times divisible by \(q\) proves that \(T\) is frequently hypercyclic. Mixing of \(T^q\) implies mixing of \(T\): for each residue \(0\le r<q\), the range of \(T^r\) is dense (mixing of \(T^q\) implies the latter has dense range), and one applies mixing of \(T^q\) to \(U_0\) and the nonempty open set \((T^r)^{-1}(V_0)\). Finally, the roots of unity in the above open eigenvalue arc are dense and have an interior accumulation point. Their associated eigenvectors, separately in each summand, span densely by analyticity, giving dense periodic points for \(T^q\), hence for \(T\). This proves Devaney chaos.

**Necessity of the dynamical threshold.** When \(R\le L\) and \(c\le1\), one has \(\|A\|\le c+R\le1\). Since \(T^q=A^{\oplus q}\), the powers of \(T\) are uniformly bounded, excluding a dense orbit. When \(R\le L\) and \(c\ge1\), one has \(c-R\ge1\) and \(A\) is invertible with \(\|A^{-1}\|\le 1/(c-R)\le1\). Hence \(\|(T^q)^n x\|\ge\|x\|\) for every \(x\) and \(n\ge0\). For a nonzero orbit of \(T\) that never becomes zero, each residue class of iterates remains bounded below by the positive norm of the corresponding first iterate; such an orbit cannot approach zero, hence is not dense. An orbit that becomes zero is also not dense. Thus hypercyclicity fails when \(R\le L\).

**Shadowing.** Messaoudi–Tofanin Neto–Tsokanos, Theorem 3.6, characterizes shadowing for arbitrary such perturbed weighted shifts by the exclusion of \(1\) from the interval between uniform lower and upper asymptotic geometric means of the products of \((d_k-\lambda)/w_k\), for every \(|\lambda|=1\). In our exact periodic case the two bounds coincide and equal
\[
\left(\frac{|\lambda^q-a^q|}{R}\right)^{1/q}.
\]
As \(\lambda\) traverses the unit circle, the numerator ranges over the entire interval \([|1-c|,1+c]=[L,U]\). Therefore shadowing holds exactly when \(R\notin[L,U]\), i.e. \(R<L\) or \(R>U\). In particular, equality at either endpoint fails shadowing. This step invokes the established shadowing characterization; the other statements above are proved independently of it.

## Verification
The power identity can be checked independently on finite leading principal sections (where all products remain upper triangular); see the included `verify.py`. The script tests nonconstant complex periodic weights, diagonal similarity conjugacy, and the exact residual identity for several periods and matrix dimensions. These finite diagnostics are **not** evidence for the infinite-dimensional spectral and dynamical conclusions, which are supplied by the proofs and cited general theorems. The comparison with the shadowing criterion uses literal products of one full period, not numerical asymptotics.

## Relationship to prior work
The arXiv preprint of Messaoudi, Tofanin Neto and Tsokanos [1] proves sufficient hypercyclicity and frequent-hypercyclicity criteria and a general shadowing characterization for perturbed weighted shifts. Its full text (especially Theorem 3.1, Corollary 3.5, and Theorem 3.6) was inspected. In the root-of-unity/periodic subclass, our sharp mixing/frequent-hypercyclicity threshold is not supplied by their sufficient weight bounds; the shadowing classification is an exact specialization of their Theorem 3.6 and is **not asserted to be a new general criterion**. The cyclotomic identity, periodic similarity invariant and sharp combined spectral/dynamical phase diagram constitute the proposed new contribution. The eigenvector implication uses the classical Godefroy–Shapiro criterion [2], and the frequent-hypercyclicity implication uses Grivaux's established theorem [3]. The ingredients' existence does not by itself establish historical priority for their combination.

## Limitations
The theorem requires exact periodicity and a primitive root of unity, and it does not classify arbitrary nonperiodic diagonal perturbations or weighted shifts. The similarity statement fixes \(q,\zeta,a,p\) and is not a classification up to arbitrary changes of those parameters. Some components are straightforward consequences of established criteria once the power identity is recognized; a broader older theorem about cyclic weighted triangular operators could subsume parts of the statement. In particular, novelty beyond the inspected literature is provisional pending independent historical-priority review. No claim of independent validation is made.

## References
1. A. Messaoudi, J. L. Tofanin Neto, and I. Tsokanos, *Dynamical Properties of Perturbed Weighted Shifts*, arXiv:2610.15023 (first posted 2026-10-10), Sections 3–5, especially Theorem 3.6. https://arxiv.org/abs/2610.15023
2. G. Godefroy and J. H. Shapiro, *Operators with dense, invariant, cyclic vector manifolds*, Journal of Functional Analysis 98 (1991), 229–269 (eigenvector criterion).
3. S. Grivaux, *A new class of frequently hypercyclic operators*, arXiv:1001.2026, 2010, subsequently Indiana University Mathematics Journal 60 (2011), 1177–1202.
4. S. Grivaux, *Sums of hypercyclic operators*, Journal of Functional Analysis 202 (2003), 486–503 (related diagonal-plus-shift setting; only bibliographic and abstract comparison).
