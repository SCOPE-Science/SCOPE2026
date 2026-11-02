# Jordan-type gaps and a motivic transfer census for cyclic Nakayama radicals

## Finding
For every field \(k\), integer \(n\ge3\), and the oriented \(n\)-cycle \(Q_n\), let \(A_n(k)=kQ_n/I^3\), where \(I\) is the arrow ideal. Its Jacobson radical \(J\) is exactly the nilpotent cone of \(A_n(k)\). Every \(x\in J\) acts nilpotently on the full \(3n\)-dimensional regular representation by left and right multiplication, \(L_x(y)=xy\) and \(R_x(y)=yx\).

Number vertices cyclically. Write \(\alpha_i:i\to i+1\), \(\beta_i=\alpha_i\alpha_{i+1}\), and \(x=\sum_{i\in\mathbb Z/n}(u_i\alpha_i+v_i\beta_i)\). Define
\[
 t(x)=\#\{i:u_i\ne0,\ u_{i+1}\ne0\},\qquad
 z(x)=\#\{i:u_i=u_{i+1}=v_i=0\}.
\]
Let \(J_r\) denote one nilpotent Jordan block of length \(r\). The **complete common Jordan type** of \(L_x\) and \(R_x\) is
\[
 \boxed{J_3^{\oplus t(x)}\oplus J_2^{\oplus(n-t(x)-z(x))}\oplus J_1^{\oplus(n-t(x)+2z(x))}.}
\]
In particular \(\operatorname{rank}L_x^2=\operatorname{rank}R_x^2=t(x)\) and \(\operatorname{rank}L_x=\operatorname{rank}R_x=n+t(x)-z(x)\). No characteristic restrictions are needed.

The distinct attainable ordered pairs \((t,z)\), and hence all Jordan types, are *exactly*
\[
 \boxed{\{(t,z)\in\mathbb Z_{\ge0}^2:t+z\le n-2\}
 \ \cup\ \{(0,n-1),(0,n),(n,0)\}.}
\]
Thus **exactly \(\binom n2+3\) Jordan types occur** over every field. The number of length-three blocks can be \(0,1,\ldots,n-2,n\), but **never \(n-1\)**. The generic type is \(J_3^{\oplus n}\).

For a finite field \(\mathbb F_q\), record the full distribution, not just its support, by
\[
 \Psi_n(q;U,V)=\sum_{x\in J(\mathbb F_q)}U^{t(x)}V^{z(x)}.
\]
Then the closed two-state transfer formula is
\[
 \boxed{\Psi_n(q;U,V)=\operatorname{tr}\left(
 \begin{pmatrix}V+q-1&q(q-1)\\q&q(q-1)U\end{pmatrix}^{n}\right).}
\]
The coefficient of \(U^tV^z\) is the exact number of nilpotent elements having the indicated Jordan type. In particular, \(\Psi_n(q;1,1)=q^{2n}\). The two roots of the transfer characteristic polynomial are generically distinct and nonzero; the sequence in \(n\) has minimal recurrence order two over \(\mathbb Q(U,V)\) for any fixed integer \(q\ge2\):
\[
 \Psi_{n+2}=a\Psi_{n+1}-b\Psi_n,
 \quad a=V+q-1+q(q-1)U,
 \quad b=q(q-1)\bigl(U(V+q-1)-q\bigr).
\]
Here the recurrence uses the transfer definition for its starting values and applies throughout the domain \(n\ge3\).

There is also a geometric refinement. Define \(\mathcal S_{t,z}\subset J\cong\mathbb A_k^{2n}\) as the locally closed locus of that Jordan type. Let \(\mathbb L=[\mathbb A^1_k]\) in the Grothendieck ring \(K_0(\mathrm{Var}_k)\). Its classes satisfy the polynomial identity
\[
 \boxed{\sum_{t,z}[\mathcal S_{t,z}]U^tV^z
 =\operatorname{tr}\left(
 \begin{pmatrix}V+\mathbb L-1&\mathbb L(\mathbb L-1)\\
 \mathbb L&\mathbb L(\mathbb L-1)U\end{pmatrix}^{n}\right).}
\]
Every \(\mathcal S_{t,z}\) has an explicit finite disjoint stratification by products of affine spaces and split tori. Its dimension is
\[
 \boxed{\dim\mathcal S_{t,z}=
 \begin{cases}
 n+t-z+\lfloor(n-t-z)/2\rfloor,&t+z\le n-2,\\
 n-z,&(t,z)=(0,n-1)\ \text{or }(0,n),\\
 2n,&(t,z)=(n,0).
 \end{cases}}
\]
No claim is made that each Jordan-type stratum is irreducible or that its scheme-theoretic closure is reduced.

## Assumptions and scope
The quiver is a directed simple cycle on \(n\ge3\) labeled vertices, with exactly one arrow from vertex \(i\) to \(i+1\) (indices modulo \(n\)). Multiplication of paths is left-to-right concatenation, and all paths of length at least three are zero in the quotient. Basis paths are the idempotents \(e_i\), the arrows \(\alpha_i\), and the length-two paths \(\beta_i\); each family has \(n\) members. Thus \(\dim_k A_n=3n\), \(J=\operatorname{span}\{\alpha_i,\beta_i\}\), and \(J^3=0\). Since \(A_n/J\cong k^n\), an element is nilpotent if and only if it belongs to \(J\). Jordan types refer to the operators on all of \(A_n\), **not** their restrictions to \(J\). All geometric statements concern locally closed, reduced strata with their natural variety structures.

## Proof
**1. A direct three-dimensional block calculation.** Each right ideal \(A_ne_j\) has ordered basis \((e_j,\alpha_{j-1},\beta_{j-2})\), preserved by \(L_x\). In that basis,
\[
 [L_x]_{A_ne_j}=\begin{pmatrix}
 0&0&0\\u_{j-1}&0&0\\v_{j-2}&u_{j-2}&0
 \end{pmatrix}.
\]
Similarly, each left ideal \(e_iA_n\) has basis \((e_i,\alpha_i,\beta_i)\), preserved by \(R_x\), with matrix
\[
 [R_x]_{e_iA_n}=\begin{pmatrix}
 0&0&0\\u_i&0&0\\v_i&u_{i+1}&0
 \end{pmatrix}.
\]
For either matrix, the nilpotent Jordan type is \(J_3\) precisely when both off-diagonal length-one coefficients are nonzero; it is \(J_1^{\oplus3}\) precisely when all three displayed coefficients vanish; and otherwise it is \(J_2\oplus J_1\). This follows directly by computing the rank and square: respectively \((2,1)\), \((0,0)\), or \((1,0)\). Reindex the left blocks by \(i=j-2\). Exchanging the two length-one coefficients does not change their zero pattern; therefore both direct sums contain exactly \(t\) length-three blocks, \(z\) zero blocks, and \(n-t-z\) blocks of type \(J_2\oplus J_1\). This proves the Jordan formula and both rank formulas without any field division.

**2. Exhaustion of the attainable types.** Let \(s_i=\mathbf1_{u_i\ne0}\). If all \(s_i\) are one, then \((t,z)=(n,0)\). If all are zero, \(t=0\) and independently prescribing which of the \(n\) coefficients \(v_i\) vanish realizes every \((0,z)\) with \(0\le z\le n\), including both exceptional terminal pairs. Otherwise, the cyclic binary word has \(c\ge1\) runs of ones and equally many runs of zeros. If it has \(r\) ones, then the number of adjacent \(11\)-edges is \(t=r-c\), and the number of adjacent \(00\)-edges is \(h=n-r-c=n-t-2c\). Exactly \(z\) of the \(h\) coordinates \(v_i\) must vanish to contribute to \(z\). Consequently \(t+z\le n-2c\le n-2\). Conversely, for every \(t+z\le n-2\), take one run of \(t+1\) ones followed by one run of \(n-t-1\) zeros; then \(h=n-t-2\ge z\). Assign nonzero values to all \(u_i\) at one-sites, zero elsewhere, and set exactly \(z\) of the \(v_i\) at \(00\)-edges to zero, the others nonzero. This realizes every such pair over every field, including \(\mathbb F_2\). The triangular region has \(n(n-1)/2\) integer pairs; adjoining the three exceptional pairs gives the announced total and sharp missing next-to-maximal length-three multiplicity.

**3. Exact finite-field transfer.** For a cyclic binary pattern \((s_i)\), each nonzero \(u_i\) has \(q-1\) possible values. At an edge \((s_i,s_{i+1})=(0,0)\), summing the choices of \(v_i\) with the weight \(V\) when it vanishes produces \(V+q-1\). At a mixed edge the \(v_i\) choices contribute \(q\), while at an \(11\)-edge they contribute \(qU\). Place the factor \(q-1\) for the next nonzero \(u_{i+1}\) on the transition to state \(1\). This gives exactly the displayed transfer matrix. Taking the trace of its \(n\)-th power imposes cyclic compatibility, and sums every \(2n\)-tuple of coefficients once. Cayley–Hamilton applied to this \(2\)-by-\(2\) matrix proves the recurrence. At \(U=V=0\), its determinant is \(-q^2(q-1)\ne0\) and its discriminant is \((q-1)^2+4q^2(q-1)\ne0\) for integer \(q\ge2\); hence the two nonzero eigenvalues are distinct under this specialization. The generic formal sequence is therefore the sum of two distinct nonzero exponentials with nonzero coefficients and cannot satisfy a first-order recurrence over \(\mathbb Q(U,V)\).

**4. Geometric strata and dimensions.** Fix a binary support \(s\) containing \(r\) ones and \(h\) adjacent \(00\)-edges, and fix a subset \(Z\) of exactly \(z\) of those edges. Impose \(u_i\ne0\) precisely at the one-sites, \(v_i=0\) at \(Z\), \(v_i\ne0\) at the remaining \(00\)-edges, and leave all other \(v_i\) unconstrained. This defines a locally closed subvariety
\[
 (\mathbb G_m)^{r+h-z}\times\mathbb A^{n-h},
\]
where the isomorphism uses only coordinate projections. All such pieces, ranging over \(s,Z\), are pairwise disjoint and cover the indicated Jordan-type locus. Taking Grothendieck classes gives one factor \(\mathbb L\) for each freely chosen affine coordinate and \(\mathbb L-1\) for each nonzero coordinate, reproducing the same transfer matrix with \(q\) replaced by \(\mathbb L\). Each piece has dimension \(n+r-z\). For a mixed word with \(c\) one-runs, \(r=t+c\) and \(h=n-t-2c\ge z\), so the largest possible \(c\) is \(\lfloor(n-t-z)/2\rfloor\). A cyclic word with that many runs exists by distributing \(t\) extra ones and \(h\) extra zeros among the positive-length runs. This yields the first displayed dimension formula; the all-zero and all-one support cases yield the two others. The dimension of a finite union is its maximal piece dimension. No scheme-theoretic assertion beyond these explicit reduced strata is used.

## Verification
`CHECKER.py` is a standalone Python 3 program requiring only the standard library. It builds the actual path multiplication matrices of \(L_x\) and \(R_x\), computes their ranks and squared ranks by Gaussian elimination over each finite field, and independently evaluates the bivariate transfer polynomial through polynomial-matrix multiplication. It exhausts \(q^{2n}\) radical elements for each of eight configurations, including non-prime \(\mathbb F_4\), whose arithmetic is implemented from \(t^2+t+1\). It checks the claimed support count and the missing Jordan rank. The recorded output is `CHECKER_OUTPUT.txt`; rerun with `python3 CHECKER.py`. The exhaustive finite tests are evidence for the corresponding configurations only. The proof above, not the tests, establishes all fields and all \(n\ge3\).

For example, when \(n=4\) and \(q=2\), the pairs \((t,z)\) with nonzero counts have the following coefficients: \((0,0):49\), \((0,1):36\), \((0,2):22\), \((0,3):4\), \((0,4):1\), \((1,0):32\), \((1,1):32\), \((2,0):64\), \((4,0):16\). They sum to \(256\). The pair \((3,0)\) is absent as predicted.

## Relationship to prior work
Shen's 2014 study establishes homological and categorical structure for Nakayama algebras and documents the relevant class of cyclic Nakayama algebras. Its theorems address singularity categories and resolution quivers, not the regular-multiplication Jordan stratification here. Iarrobino, Macias Marques and McDaniel develop the theory and geometric significance of Jordan types of multiplication in Artinian commutative algebras, including general rank-to-Jordan relations and Jordan-type loci; the present theorem gives a new, explicit noncommutative cyclic Nakayama family rather than claiming those general principles. Earlier square-zero enumeration for cyclic Nakayama algebras with radical fourth power zero concerns the different question \(x^2=0\) in a different Loewy length; its methods do not by themselves yield the present all-type motive and sharp support classification. The two-state transfer-matrix identity uses elementary weighted-word enumeration, which is not itself claimed as new. The claimed contribution is the complete regular Jordan-type classification, the exact set and number of possible partitions, the arithmetic and motivic distributions, and their geometric dimensions for this family.

## Limitations
Only the standard oriented cyclic Nakayama algebras \(kQ_n/I^3\), with \(n\ge3\), are covered. Jordan types of arbitrary diagonal (nonnilpotent) elements, arbitrary Kupisch-series Nakayama algebras, higher Loewy lengths, orbit closures, and nonreduced scheme structures are not classified. The result is a mathematical proof plus finite checks, not an independent peer review or certification of historical publication priority. Unlocated stronger literature could affect the originality assessment.

## References
1. D. Shen, *The singularity category of a Nakayama algebra*, first arXiv submission 9 April 2014, arXiv:1404.2451; primary MSC 16G10. https://arxiv.org/abs/1404.2451
2. A. Iarrobino, P. Macias Marques and C. McDaniel, *Artinian algebras and Jordan type*, first arXiv submission 21 February 2018, arXiv:1802.07383. https://arxiv.org/abs/1802.07383
3. N. Altafi, A. Iarrobino and P. Macias Marques, *Jordan type of an Artinian algebra, a survey*, arXiv:2307.00957 (2023). https://arxiv.org/abs/2307.00957
