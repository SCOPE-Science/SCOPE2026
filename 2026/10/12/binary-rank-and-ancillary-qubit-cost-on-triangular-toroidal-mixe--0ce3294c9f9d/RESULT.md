# Binary rank and ancillary-qubit cost on triangular toroidal mixed graphs

## Finding

For integers \(m,n\geq3\), let \(G_{m,n}\) be the simple undirected graph on \(\mathbb Z_m\times\mathbb Z_n\) whose neighbors of \((a,b)\) are the six distinct vertices reached by the displacements
\[
(1,0),\quad(-1,0),\quad(0,1),\quad(0,-1),\quad(1,1),\quad(-1,-1).
\]
Orient each edge exactly once, in any manner, and let \(A\) be the directed adjacency matrix over \(\mathbb F_2\). The binary commutator matrix \(Q=A+A^{\mathsf T}\) equals the undirected adjacency matrix of \(G_{m,n}\). With \(g=\gcd(m,n)\), its nullity and rank are exactly
\[
\boxed{\dim_{\mathbb F_2}\ker Q=m+n+g-2,\qquad
\operatorname{rank}_{\mathbb F_2}Q=mn-m-n-g+2.}
\]
Consequently, the minimum number of ancillary qubits needed for a commuting stabilizer extension in the mixed-graph-state construction of Riera, Parker, and Stănică is, for every orientation,
\[
\boxed{e(G_{m,n})=\frac{mn-m-n-\gcd(m,n)+2}{2}.}
\]
In particular, for coprime periods this cost is \((m-1)(n-1)/2\). The formula holds without odd-period or semisimplicity assumptions.

## Assumptions and scope

The graph is the six-neighbor periodic triangular lattice defined above, with two independent rectangular periods and no loops or doubled undirected edges. The restrictions \(m,n\geq3\) guarantee six distinct neighbors. Every edge is directed exactly once; no undirected edge is superposed on a directed edge. The rank is taken in characteristic two, not over the reals or complexes. The ancillary-qubit interpretation uses the precise commuting-extension resource measure proved in Lemma 4.1 of Riera, Parker, and Stănică; it does not assert equivalence to other physical resource metrics.

## Proof

Work over \(\mathbb F_2\) on the vector space \(V=\mathbb F_2^{\mathbb Z_m\times\mathbb Z_n}\). Let \(X,Y\) be the invertible, commuting cyclic translation operators in the first and second coordinates. The triangular adjacency operator is
\[
Q=X+X^{-1}+Y+Y^{-1}+XY+(XY)^{-1}.
\]
In the Laurent polynomial ring over \(\mathbb F_2\), direct multiplication gives
\[
\boxed{Q=X^{-1}Y^{-1}(I+X)(I+Y)(I+XY).}\tag{1}
\]
Indeed, the product \((1+x)(1+y)(1+xy)\) has monomials \(x^2y,xy^2,x,y,x^2y^2,1\); the two \(xy\) terms cancel in characteristic two. Division by \(xy\) produces precisely the six required shifts.

Set \(B=(I+X)(I+Y)\) and \(W=\operatorname{im}B\). On one cyclic coordinate, \(\operatorname{im}(I+X)\) is exactly the codimension-one subspace of vectors whose coordinates sum to zero: every image has zero sum, and the kernel of \(I+X\) consists of the constant vectors, of dimension one. The same applies to \(I+Y\). Taking the tensor product of these two images shows that \(W\) consists exactly of arrays for which **every row sum and every column sum vanishes** in \(\mathbb F_2\). Hence
\[
\dim W=(m-1)(n-1).\tag{2}
\]

The kernel of \(I+XY\) consists of functions constant on the orbits of simultaneous translation \((a,b)\mapsto(a+1,b+1)\). There are exactly \(g=\gcd(m,n)\) such orbits, labeled by the residue of \(b-a\) modulo \(g\). Every member of the kernel therefore has the form
\[
f(a,b)=c_{b-a\pmod g},\qquad (c_0,\ldots,c_{g-1})\in\mathbb F_2^g.
\]
Put \(C=\sum_{r=0}^{g-1}c_r\). Every row sum of \(f\) equals \((n/g)C\), and every column sum equals \((m/g)C\), each interpreted in \(\mathbb F_2\). Because \(m/g\) and \(n/g\) are coprime, at least one is odd. Both families of sums therefore vanish **if and only if** \(C=0\). Consequently,
\[
\dim\bigl(W\cap\ker(I+XY)\bigr)=g-1.\tag{3}
\]

The invertible factor \(X^{-1}Y^{-1}\) does not affect rank, while the factors in (1) commute. Applying rank-nullity to the restriction of \(I+XY\) to \(W\), and using (2)–(3), gives
\[
\operatorname{rank}Q=\dim W-\dim\bigl(W\cap\ker(I+XY)\bigr)
=(m-1)(n-1)-(g-1).
\]
Subtracting this from \(mn\) gives the nullity formula. Finally, for any orientation of each undirected edge exactly once, \(A+A^{\mathsf T}=Q\) in \(\mathbb F_2\); Lemma 4.1 of Riera, Parker, and Stănică identifies the minimal commuting-extension ancillary count with \(\operatorname{rank}(Q)/2\). This proves the asserted formula for every orientation. The expression is integral because \(Q\) is alternating, so its binary rank is even. \(\square\)

## Verification

The accompanying standalone standard-library program `verify.py`, executable with `python3 verify.py`, performs direct binary Gaussian elimination for **all 529 ordered parameter pairs** \(3\leq m,n\leq25\), including both even and odd periods. It independently computes the parity constraints in the diagonal-orbit argument for the same pairs, checks the Laurent-polynomial factorization, and verifies six nontrivial edge orientations by constructing \(A+A^{\mathsf T}\) explicitly. The expected successful program output is:

```text
VERIFY_OK symbolic_factorization=1 all_parity_rank_tests=529 diagonal_orbit_parity_tests=529 orientation_tests=6 m_n_each_3_to_25=true
```

For illustration, the exact rank and ancillary pairs \((\operatorname{rank}_{\mathbb F_2}Q,e)\) are \((2,1)\) for \((m,n)=(3,3)\), \((6,3)\) for \((4,4)\), \((8,4)\) for \((3,5)\), and \((34,17)\) for \((6,8)\). These computations corroborate the unrestricted algebraic proof; they do not prove the infinite parameter family by enumeration.

## Relationship to prior work

Riera, Parker, and Stănică supply the **general** mixed-graph commutation problem and the half-binary-rank ancillary rule; that rule is used as a cited premise here, not claimed as new. The additional content is the closed all-period binary rank formula for an explicit six-neighbor, two-dimensional periodic graph family, including the diagonal winding correction \(\gcd(m,n)-1\). Their paper's inspected mixed-graph-state analysis does not derive such a periodic-lattice rank law.

Peters, Goldwasser, and Young analyze characteristic-two Lights Out questions for **Cartesian products**, whose four-neighbor toroidal adjacency lacks the two diagonal shifts of \(G_{m,n}\). Their solvability criteria do not imply the rank formula proved here. More general results about symmetric matrices over \(\mathbb F_2\) establish useful structural properties but likewise do not supply the specific diagonal-orbit count. No claim of global bibliographic uniqueness is made.

## Limitations

The exact family has six specified displacements and untwisted rectangular toroidal identifications; arbitrary skew-periodic quotients, different diagonal orientations, weighted edges, characteristic other than two, or graphs with duplicated neighbor steps are not classified here. The proof yields a rank/resource identity, not a circuit-depth optimization or a physical implementation claim. Finite checks are supplementary. Literature indexing under cellular automata or modular harmonic functions may conceal equivalent treatments; independent audit has not been performed.

## References

1. Constanza Riera, Matthew G. Parker, and Pantelimon Stănică, *Quantum states associated to mixed graphs and their algebraic characterization*, Advances in Mathematics of Communications **17** (2023), 660–680, early access 2021-05-10, DOI: 10.3934/amc.2021015. Relevant prior input: Lemma 4.1 and the mixed-graph-state construction. Author-hosted manuscript: https://faculty.nps.edu/pstanica/research/2021AMCNewMixed.pdf
2. Travis Peters, John Goldwasser, and Michael Young, *LIGHTS OUT! on Cartesian Products*, Electronic Journal of Linear Algebra **32** (2017), 464–474, DOI: 10.13001/1081-3810.3483.
3. Igor Minevich, *Symmetric Matrices over F2 and the Lights Out Problem*, arXiv:1206.2973 (2012). General structural background; no triangular-torus rank classification is asserted here.
