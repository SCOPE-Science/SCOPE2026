# Four Cartier strata and ten isogeny classes of binary plane-filling quintics

## Finding
Among all geometrically smooth plane quintics \(C\subset\mathbf P^2_{\mathbf F_2}\) containing every one of the seven rational points of their plane, the Jacobian \(2\)-rank and \(a\)-number take **exactly** the four pairs
\[
(f_2,a)\in\{(2,3),(2,1),(5,1),(6,0)\}.
\]
The respective numbers of binary defining equations, counted without projective scalar duplication, are \(168,252,336,756\). They occupy respectively \(1,2,2,5\) orbits of the ambient group \(\operatorname{PGL}_3(\mathbf F_2)\). Hence the minimum possible \(2\)-rank is \(2\), and \(2\)-ranks \(0,1,3,4\) cannot occur. Moreover, the ten ambient orbits have pairwise different Weil numerators; their Jacobians occupy **exactly ten distinct \(\mathbf F_2\)-isogeny classes**. These also distinguish ten abstract \(\mathbf F_2\)-isomorphism classes of curves (without classifying geometric isomorphisms over the algebraic closure).

## Assumptions and scope
The ground field is \(\mathbf F_2\). Consider every nonzero homogeneous polynomial of total degree \(5\) in \(X,Y,Z\), with coefficients in this field, vanishing at each of the seven points of \(\mathbf P^2(\mathbf F_2)\); keep exactly those whose projective zero loci are geometrically nonsingular. These are smooth curves of genus \(6=(5-1)(5-2)/2\). There are \(21\) degree-five monomials and seven independent point-value conditions, so the vanishing subspace has dimension \(14\) and contains \(2^{14}-1=16383\) nonzero equations. Projective scalar multiplication is trivial over \(\mathbf F_2\). The statement concerns this embedded family and its Jacobians, not all genus-six curves.

For a curve \(C\), \(f_2\) is the dimension of its geometric \(2\)-torsion group of rational points, and \(a=\dim_{\overline{\mathbf F}_2}\operatorname{Hom}(\alpha_2,\operatorname{Jac}(C))\). The Weil numerator is \(L_C(T)=\exp(\sum_{n\ge1}(N_n-(2^n+1))T^n/n)\), with \(N_n=\#C(\mathbf F_{2^n})\).

## Proof
Use the descending lexicographic monomial list \(M_i=X^{a_i}Y^{b_i}Z^{c_i}\), indexed by \(0\le i\le20\), with \(a_i+b_i+c_i=5\). The integer `mask` describes the equation \(F=\sum_{i=0}^{20}\epsilon_i M_i\), where the binary digits \(\epsilon_i\) are the bits of that integer. Thus every representative is explicit and unambiguous. All coefficient arithmetic is exact over \(\mathbf F_2\).

First, row reduction on the seven evaluation vectors gives a \(14\)-dimensional kernel. Enumerate its \(16383\) nonzero members and partition them under coordinate swaps and the shear \((X,Y,Z)\mapsto(X+Y,Y,Z)\); together these generate \(\operatorname{PGL}_3(\mathbf F_2)\) of order \(168\). For every orbit representative, form the three homogeneous partial derivatives. Because \(5\) is odd in characteristic two, Euler's identity says \(F=X F_X+Y F_Y+Z F_Z\). Thus on each of the three affine charts, the derivatives have a simultaneous zero if and only if the projective curve is singular there. Compute Gröbner bases over \(\mathbf F_2\) on all three charts: each ideal is the unit ideal exactly when the chart has no common derivative zero over the algebraic closure. Precisely ten smooth group orbits remain, with the sizes in the table below (eight of size \(168\), two of size \(84\)). Their total is \(1512\). No bounded extension-field smoothness heuristic enters the argument.

The classical plane-curve Hasse–Witt coefficient formula can also be derived directly from the exact sequence \(0\to\mathcal O_{\mathbf P^2}(-5)\to\mathcal O_{\mathbf P^2}\to\mathcal O_C\to0\). Via \(H^1(C,\mathcal O_C)\cong H^2(\mathbf P^2,\mathcal O(-5))\), use the six Čech classes corresponding to \(X^{-a-1}Y^{-b-1}Z^{-c-1}\), with \(a+b+c=2\). Frobenius followed by multiplication by \(F\) gives a matrix whose transpose has entries
\[
H_{\mathbf a,\mathbf b}=[X^{2a_x-b_x+1}Y^{2a_y-b_y+1}Z^{2a_z-b_z+1}]F
\]
for the degree-two exponent triples \(\mathbf a,\mathbf b\); coefficients with a negative exponent are zero. This is a \(6\)-by-\(6\) matrix over \(\mathbf F_2\). The \(a\)-number equals \(6-\operatorname{rank}H\), and the \(2\)-rank is the stable rank \(\operatorname{rank}H^6\), since coefficients lie in the prime field. Exact binary row reduction for all ten representatives yields the four stated pairs and orbit-weighted counts.

For independent arithmetic discrimination, count all projective zeros over \(\mathbf F_{2^n}\) for \(1\le n\le6\), using finite fields presented by irreducible binary polynomials of degrees \(n\), and compute \(c_1,\ldots,c_6\) of \(L_C(T)=\sum_{k=0}^{12}c_kT^k\) via Newton identities. The remaining coefficients are determined by \(c_{12-k}=2^{6-k}c_k\) for \(0\le k\le5\). The complete ten representative certificates are:

| Equation mask | Ambient orbit | \(2\)-rank | \(a\)-number | \(c_1,\ldots,c_6\) |
|---:|---:|---:|---:|---|
| `213034` | 168 | 2 | 3 | \(4,11,22,38,58,84\) |
| `213150` | 84 | 6 | 0 | \(4,10,18,24,26,33\) |
| `213334` | 168 | 6 | 0 | \(4,12,27,52,87,129\) |
| `213658` | 168 | 6 | 0 | \(4,10,21,39,62,89\) |
| `213756` | 168 | 6 | 0 | \(4,10,18,27,35,47\) |
| `215182` | 168 | 5 | 1 | \(4,11,23,40,63,90\) |
| `215210` | 168 | 2 | 1 | \(4,11,24,46,76,114\) |
| `215310` | 168 | 6 | 0 | \(4,11,24,47,78,117\) |
| `215482` | 84 | 2 | 1 | \(4,11,22,38,56,80\) |
| `221388` | 168 | 5 | 1 | \(4,11,22,37,55,78\) |


All ten displayed six-tuples are distinct, hence the full Weil numerators are distinct. Tate's finite-field isogeny theorem distinguishes the ten Jacobian isogeny classes. Any \(\mathbf F_2\)-curve isomorphism preserves its zeta function, so these ten orbits remain distinct even as abstract \(\mathbf F_2\)-curves. Every smooth equation is in one of the displayed ambient orbits, completing the classification.

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed. The standalone program generates the entire \(14\)-dimensional equation space from point-evaluation constraints, constructs the \(\operatorname{PGL}_3(\mathbf F_2)\)-orbits, checks geometric smoothness using exact Gröbner bases, builds the six-dimensional Hasse–Witt matrices, computes all stable ranks, counts points over extensions through degree \(6\), recovers the Weil numerators, and asserts the stated type counts, ten pairwise distinct numerators, and agreement between stable ranks and their mod-two zeta reductions. An actual execution completed with `CERTIFIED: 1512 smooth equations, ten distinct zeta polynomials, and complete Cartier stratification`.

## Relationship to prior work
Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields* (arXiv:2307.03072, first version 6 July 2023), study degree \(q+3\) plane-filling curves, including a special characteristic-two construction and smoothness criteria. Their eight-page preprint does not give the complete binary-quintic Jacobian \(2\)-rank, \(a\)-number, and Weil-numerator classification. The previously available exact census of \(1512\) smooth equations and ten ambient orbits is **not** claimed as novel here. The assessed contribution is the complete arithmetic stratification and separation of all ten rational Jacobian isogeny classes.

## Limitations
The result does not classify arbitrary genus-six curves or geometric isomorphisms after extending the field, and it does not determine Newton polygons beyond the \(2\)-rank information. The novelty assessment is limited by the possibility of an unindexed equivalent calculation. All computations are exact and finite, but independent external validation has not been performed.

## References
- Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (6 July 2023), https://arxiv.org/abs/2307.03072.
- Masaaki Homma and Seon Jeong Kim, *Nonsingular plane filling curves of minimum degree over a finite field*, 2013; contextual comparison as referenced in arXiv:2307.03072. Their minimum-degree problem is \(q+2\), rather than the degree-five family classified here.
- The plane-curve Hasse–Witt coefficient method follows from Frobenius on \(H^2(\mathbf P^2,\mathcal O(-5))\), as explicitly derived above.
