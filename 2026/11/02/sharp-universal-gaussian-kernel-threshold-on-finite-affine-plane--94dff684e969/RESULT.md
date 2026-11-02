# Sharp universal Gaussian-kernel threshold on finite affine-plane incidence graphs

## Finding
Let \(\Pi\) be **any** finite affine plane of order \(q\ge2\), whenever such a plane exists. Let \(X\) consist of all \(q^2\) points and all \(q(q+1)\) lines of \(\Pi\), equipped with the shortest-path distance \(d\) in the point–line incidence graph. For \(t>0\) and \(p\ge0\), put
\[
K_{t,p}(x,y)=\exp(-t\,d(x,y)^p),
\]
with \(d(x,x)^0=0\) and \(d(x,y)^0=1\) for distinct points and lines. Define
\[
\alpha_q=\log_2\!\left(\frac q{q-1}\right).
\]
Then \(K_{t,p}\) is positive semidefinite **for every \(t>0\)** precisely when \(0\le p\le\alpha_q\). Equivalently, the powered-distance matrix \(D_p=(d(x,y)^p)_{x,y\in X}\) is conditionally negative semidefinite precisely for these exponents.

For \(0\le p<\alpha_q\), conditional negativity is strict. At \(p=\alpha_q\), the nullity on the real zero-sum coefficient space is exactly \(q\) for \(q\ge3\), but exactly \(5\) for \(q=2\). Consequently the minimum Euclidean dimension of an embedding with squared Euclidean distances \(d(x,y)^{\alpha_q}\) is
\[
\dim_{\mathrm{Euc}}=
\begin{cases}
4,&q=2,\\
2q^2-1,&q\ge3.
\end{cases}
\]
At all strictly subcritical exponents the minimum squared-Euclidean embedding dimension is \(2q^2+q-1\). Along existing affine-plane orders tending to infinity,
\[
\alpha_q=\frac1{q\log2}+\frac1{2q^2\log2}+O(q^{-3}).
\]
The assertion uses only the affine-plane incidence axioms, not coordinates or Desarguesian symmetry.

## Assumptions and scope
A finite affine plane of order \(q\) has \(q^2\) points; its \(q(q+1)\) lines split into \(q+1\) parallel classes of \(q\) mutually disjoint lines; any two points determine one line; each point is on \(q+1\) lines. Distinct points have graph distance \(2\). Distinct lines have graph distance \(2\) if they intersect and \(4\) if they are parallel. A point and a line have distance \(1\) if incident and \(3\) otherwise. The proof is conditional on the plane's existence; no assertion that planes exist for every integer \(q\) is made.

For any finite symmetric matrix \(D\) with zero diagonal, conditional negative semidefiniteness means \(z^{\mathsf T}Dz\le0\) for all real \(z\) satisfying \(\sum_{x\in X}z_x=0\). Write \(J=I-|X|^{-1}{\bf1}{\bf1}^{\mathsf T}\). The rank of \(-\tfrac12JD_pJ\) is the minimal Euclidean embedding dimension for the squared-distance matrix \(D_p\) whenever conditional negative semidefiniteness holds.

## Proof
Put \(a=2^p\), \(b=4^p=a^2\), and \(c=3^p\). Let \(B\) be the point-by-line incidence matrix, and let \(H\) be the adjacency matrix on lines that joins two different lines precisely when they are in the same parallel class. Let \(J_{r,s}\) be the all-ones matrix of size \(r\)-by-\(s\). The elementary affine-plane axioms imply the exact identities
\[
BB^{\mathsf T}=qI_{q^2}+J_{q^2,q^2},\qquad
B^{\mathsf T}B=(q-1)I_{q(q+1)}+J_{q(q+1),q(q+1)}-H.
\]
By the distance classification above,
\[
D_p=\begin{pmatrix}
a(J_{q^2,q^2}-I_{q^2})&cJ_{q^2,q(q+1)}+(1-c)B\\
cJ_{q(q+1),q^2}+(1-c)B^{\mathsf T}&a(J_{q(q+1),q(q+1)}-I_{q(q+1)})+(b-a)H
\end{pmatrix}.
\]

We orthogonally decompose the real zero-sum coefficient space (dimension \(2q^2+q-1\)) into three invariant sectors.

**Parallel-class contrasts (dimension \(q\)).** Take vectors supported on lines, constant inside each parallel class, and summing to zero over all lines. Since \(B\) kills these vectors and \(H\) acts as multiplication by \(q-1\), the eigenvalue of the quadratic form is
\[
L_q(p)=(q-1)b-qa=a((q-1)a-q).
\]
It is negative for \(p<\alpha_q\), zero at \(p=\alpha_q\), and positive for \(p>\alpha_q\). Thus the proposed upper threshold is necessary, and for every exponent above it the powered distance matrix is not conditionally negative semidefinite.

**Paired point/line contrasts (dimension \(2(q^2-1)\)).** On zero-sum point vectors, \(BB^{\mathsf T}\) acts as \(qI\). Their normalized images under \(B^{\mathsf T}\) are line vectors with zero sum in each parallel class, on which \(H=-I\). Thus this sector consists of \(q^2-1\) orthogonal copies of
\[
M_q(p)=\begin{pmatrix}-a&\sqrt q(1-c)\\\sqrt q(1-c)&-b\end{pmatrix}.
\]
Both diagonal entries are strictly negative; this block is negative definite exactly when
\[
F_q(p)=ab-q(c-1)^2>0.
\]
For \(0\le p\le\alpha_q\le1\), set \(g(p)=(3^p-1)/8^{p/2}\). As
\[
g(p)=(3/\sqrt8)^p-(1/\sqrt8)^p,
\]
\(g\) is strictly increasing for \(p\ge0\). At the endpoint, \(q=a/(a-1)\), so
\[
qg(\alpha_q)^2=\frac{(3^p-1)^2}{a^2(a-1)}\bigg|_{p=\alpha_q}.
\]
For \(0<p\le1\), define \(R(p)=(3^p-1)^2/[2^{2p}(2^p-1)]\). The ratio \((3^p-1)/(2^p-1)\) increases strictly with \(p\), since \(w/(1-e^{-wp})\) increases with \(w>0\). The other factor \((2^p-1)/2^{2p}\) increases on \((0,1]\). Hence \(R(p)\) increases strictly to \(R(1)=1\). Therefore \(F_q(p)>0\) throughout the closed interval \([0,\alpha_q]\) when \(q\ge3\); for \(q=2\), \(\alpha_2=1\) and \(F_2(p)>0\) except exactly at the endpoint, where \(F_2(1)=0\).

**Global point-versus-line contrast (dimension \(1\)).** Give each point coefficient \(u\) and each line coefficient \(-qu/(q+1)\), so the total sum is zero. Dividing the quadratic form by \(q^2u^2\) gives
\[
E_q(p)=a(q^2-1)+\frac{q}{q+1}\bigl((q-1)b+q^2a\bigr)-\frac{2q}{q+1}\bigl((q+1)+(q^2-1)c\bigr).
\]
For \(0\le p\le1\), concavity yields \(c=3^p\ge(a+b)/2\). Substitution gives the upper bound
\[
E_q(p)\le U_q(a)=\frac{a(q^3+q^2-1)+a^2(-q^3+q^2)-2q^2-2q}{q+1}.
\]
For \(q\ge3\), \(U_q\) is strictly concave in \(a\), with \(U'_q(1)=(-q^3+3q^2-1)/(q+1)<0\) and \(U_q(1)=-(2q+1)/(q+1)<0\). Thus \(E_q(p)<0\) whenever \(a\ge1\). For \(q=2\), \(U_2(a)=(-4a^2+11a-12)/3<0\) for every real \(a\), since the quadratic has negative discriminant. This global sector is therefore always strictly negative at all permitted exponents.

The sector dimensions sum to \(q+2(q^2-1)+1=2q^2+q-1\). Combining their signs proves the complete conditional-negative-type interval. Exactly the \(q\)-dimensional parallel-class contrast space is null at the endpoint for \(q\ge3\). For \(q=2\), the \(q^2-1=3\) paired blocks each gain a one-dimensional kernel at \(p=1\), giving endpoint nullity \(2+3=5\). All strictly smaller exponents have no zero directions on the zero-sum space.

Finally, Schoenberg's positive-definiteness theorem converts conditional negativity of \(D_p\) into positivity of \(\exp(-tD_p)\) for all \(t>0\). Conversely, if \(z^{\mathsf T}D_pz>0\) with \(\sum z=0\), then for small \(t>0\), \(z^{\mathsf T}\exp(-tD_p)z=-t z^{\mathsf T}D_pz+O(t^2)<0\). The centered Gram rank gives the stated embedding dimensions. The expansion of \(\alpha_q=-\log(1-1/q)/\log2\) proves the asymptotic statement.

## Verification
The standalone file `checker.py` independently constructs affine planes over prime fields of orders \(2,3,5,7\) and the field of order \(4\). It verifies the exact incidence identities, and for orders at most five independently reconstructs every graph distance using breadth-first search. For each order it directly diagonalizes the centered powered-distance matrix at five exponents, including the exact threshold, and checks the predicted endpoint nullity and positivity above the threshold. Run `python checker.py` with NumPy installed. The finite tests are corroboration only; the proof above treats every existing finite affine plane, including non-Desarguesian ones.

## Relationship to prior work
Schoenberg's theorem relates universal Gaussian positive definiteness to conditional negative type. Li and Weston, *Strict p-negative type of a metric space* (arXiv:0901.0695, first version 2009-01-06), prove general strictness below an attained exponent; their Theorem 5.4 does not evaluate this affine-plane family. Sánchez, *On the supremal p-negative type of a finite metric space* (arXiv:1108.0451, first version 2011-08-02), gives a general finite-distance-matrix method and calculates complete bipartite graph values; its graph application has only distances \(0,1,2\), whereas the present incidence metric has the essential parallel-line distance \(4\). The novelty assessed here is the explicit all-orders threshold, complete endpoint nullity and embedding dimensions, and their independence from the coordinate model of the affine plane. General methods and Schoenberg's equivalence are not claimed as new.

## Limitations
The theorem is for unit-edge shortest-path metrics on finite affine-plane incidence graphs and for universal positivity at **all** Gaussian scales \(t>0\); it does not classify positivity at one fixed scale beyond the threshold. It assumes existence of an affine plane of the stated order, not existence at every integer. The elementary sector argument is self-contained, but the kernel equivalence invokes Schoenberg's classical theorem. The historical coverage review is bounded, so an equivalent older theorem on resolvable-design incidence metrics cannot be excluded without further independent literature review. No independent audit has been performed.

## References
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, initially posted 2009-01-06; in particular Theorems 5.2 and 5.4.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, initially posted 2011-08-02; in particular Sections 2 and 3.
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44** (1938), 522–536 (classical equivalence, discussed in the two cited preprints).
