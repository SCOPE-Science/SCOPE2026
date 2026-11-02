# Coordinate conjugacy, exact retraction counts and logarithmic codimension in modular elementary-abelian group algebras

## Finding
Let \(p\) be prime, \(q=p^f\) with \(f\ge1\), and \(d\ge1\). Write
\[
R_d=\mathbb F_q[(C_p)^d]\cong \mathbb F_q[x_1,\ldots,x_d]/(x_1^p,\ldots,x_d^p).
\]
Endomorphisms below are unital \(\mathbb F_q\)-algebra maps. Every idempotent endomorphism \(e\) is conjugate, by an \(\mathbb F_q\)-algebra automorphism, to precisely one of the coordinate projections \(e_k\), \(0\le k\le d\), taking the first \(k\) variables to themselves and the other variables to zero. Consequently its image has \(\mathbb F_q\)-dimension \(p^k\); every such dimension occurs. The number with this image dimension is exactly
\[
\boxed{N_{d,k}(p,q)={d\brack k}_q\,q^{\,k(p^d-p^k)+(d-k)(p^k-k-1)}}
\quad(0\le k\le d),
\]
where \({d\brack k}_q=\prod_{j=0}^{k-1}(q^{d-j}-1)/(q^{k-j}-1)\) is a Gaussian binomial coefficient. In particular \(N_{d,0}=N_{d,d}=1\). The total number of idempotents is \(\sum_{k=0}^dN_{d,k}\), whereas the entire endomorphism monoid has \(q^{d(p^d-1)}\) elements.

For fixed \(p,q\), choose uniformly among *idempotent algebra endomorphisms* and let \(K_d\) denote the unique \(k\) such that the image has dimension \(p^k\). Set \(B_d=d-K_d\), \(b_d=\lfloor\log_p d\rfloor\). Then
\[
\boxed{\Pr\bigl(B_d\in\{b_d-1,b_d,b_d+1\}\bigr)\longrightarrow1\quad(d\to\infty)}.
\]
Thus \(B_d=\log_p d+O_{\mathsf P}(1)\), and the dimension of a typical retract image is \(\Theta_{\mathsf P}(p^d/d)\), rather than a constant fraction of the ambient algebra dimension. The phrase \(\Theta_{\mathsf P}\) here means that the ratio is bounded above and below by fixed positive constants with probability tending to one.

## Assumptions and scope
The coefficient field is a fixed finite field of characteristic \(p\); all morphisms are unital and fix its coefficients. The algebra is the commutative modular group algebra of an elementary abelian group, not its abstract additive group or its group of units. The image rank refers to dimension as a vector space over \(\mathbb F_q\), with the identity map of rank \(p^d\) and augmentation of rank one. The asymptotic keeps \(p,q\) fixed while \(d\) grows; it concerns the uniform distribution on idempotent maps, not on all algebra endomorphisms or on group endomorphisms.

## Proof
**1. A free nilpotent-coordinate property.** Let \(\mathfrak m=(x_1,\ldots,x_d)\). The residue algebra is \(R_d/\mathfrak m=\mathbb F_q\), and \(R_d\) has vector-space dimension \(P=p^d\), with basis the monomials whose individual exponents lie between zero and \(p-1\). Every \(u\in\mathfrak m\) has \(u^p=0\): in characteristic \(p\), the \(p\)-th power of a sum is the sum of the \(p\)-th powers, and each nonconstant monomial has \(p\)-th power zero. Thus any ordered \(d\)-tuple in \(\mathfrak m^d\) freely defines a unital algebra endomorphism. Its linear part on \(\mathfrak m/\mathfrak m^2\) is any \(d\)-square matrix. Such an endomorphism is invertible precisely when this matrix is invertible: in the invertible case the induced maps on every quotient \(\mathfrak m^j/\mathfrak m^{j+1}\) are surjective, by products of degree-one generators, hence the endomorphism is surjective and therefore bijective. This also yields
\[
|\operatorname{Aut}(R_d)|=|\operatorname{GL}_d(\mathbb F_q)|q^{d(P-1-d)},
\qquad |\operatorname{End}(R_d)|=q^{d(P-1)}.
\]

**2. Conjugacy of retractions.** For \(e^2=e\), its linear part is an idempotent matrix. After an invertible linear change of variables (which extends to an algebra automorphism by the previous paragraph), assume that this matrix is \(\mathrm{diag}(I_k,0)\). Define an algebra endomorphism \(\phi\) on generators by
\[
\phi(x_i)=e(x_i)\ (i\le k),\qquad
\phi(x_j)=x_j-e(x_j)\ (j>k).
\]
All images lie in \(\mathfrak m\), and their linear terms are exactly the original variables, so \(\phi\) is an automorphism. For \(i\le k\), \(e\phi(x_i)=\phi(x_i)\), while for \(j>k\), \(e\phi(x_j)=0\). Hence \(e\phi=\phi e_k\), or \(e=\phi e_k\phi^{-1}\). The integer \(k\) is uniquely determined by the induced linear rank and by \(\dim\operatorname{im}(e)=p^k\).

**3. Counting stabilizers.** Put \(b=d-k\) and \(K=p^k\). An automorphism \(\psi\) commutes with \(e_k\) if and only if its first \(k\) generator images lie in the coordinate subalgebra \(R_k\), and its remaining \(b\) generator images lie in \(\ker(e_k)\). The dimensions of the respective allowable nilpotent coefficient spaces are \(K-1\) and \(P-K\). The invertibility requirement reduces to two independent diagonal linear blocks of sizes \(k\) and \(b\). Therefore
\[
|C_{\operatorname{Aut}(R_d)}(e_k)|
=|\operatorname{GL}_k(q)|\,|\operatorname{GL}_b(q)|
q^{k(K-1-k)+b(P-K-b)}.
\]
Orbit-stabilizer gives
\[
N_{d,k}=
\frac{|\operatorname{GL}_d(q)|}{|\operatorname{GL}_k(q)|\,|\operatorname{GL}_b(q)|}
q^{d(P-1-d)-k(K-1-k)-b(P-K-b)}.
\]
Use \(|\operatorname{GL}_d(q)|/(|\operatorname{GL}_k(q)||\operatorname{GL}_b(q)|)={d\brack k}_q q^{kb}\), and simplify the exponent, obtaining the boxed formula. The formulas include \(k=0\) and \(k=d\) by the conventions \(\operatorname{GL}_0(q)=\{1\}\) and empty products equal one.

**4. Localization of the typical codimension.** Let \(b=d-k\) and \(P=p^d\). The exponent in the boxed formula becomes
\[
H_d(b)=P\underbrace{\bigl((d-b)-(d-2b)p^{-b}\bigr)}_{h_d(b)}-b(d-b+1).
\]
The Gaussian coefficient satisfies \(1\le {d\brack b}_q\le q^{d^2}\), so its contribution to \(\log_qN_{d,d-b}\) is between zero and \(d^2\). Moreover, for \(0\le b<d\),
\[
h_d(b+1)-h_d(b)=-1+\frac{(p-1)(d-2b)+2}{p^{b+1}}.
\]
Take \(b_0=\lfloor\log_p d\rfloor\). For all sufficiently large \(d\), this difference is at least \(1/2\) whenever \(b\le b_0-2\), and at most \(-1/(2p)\) whenever \(b\ge b_0+1\). To check the first inequality, use \(d\ge p^{b_0}\), \(p^{b+1}\le p^{b_0-1}\), and \(b\le b_0-2=o(d)\); its right-hand side is asymptotically bounded below by \(-1+p(p-1)\ge1\). For the second, use \(d<p^{b_0+1}\), \(p^{b+1}\ge p^{b_0+2}\), and \(-2b\le0\), giving an upper bound \(-1+(p-1)/p+o(1)\). Therefore any \(b\) outside the three-element window \(W_d=\{b_0-1,b_0,b_0+1\}\cap\{0,\ldots,d\}\) has \(h_d(b)\) at least \(1/(2p)\) below some \(h_d(c)\), \(c\in W_d\). The bounded lower-order terms contribute at most \(O(d^2)\) to log-ratios, whence
\[
\Pr(B_d\notin W_d)\le(d+1)q^{-p^d/(2p)+O(d^2)}\longrightarrow0.
\]
Since \(p^{b_0}\le d<p^{b_0+1}\), the claimed tight logarithmic codimension and retract-image dimension scale follow.

## Verification
The accompanying standalone `verify.py` enumerates all unital algebra endomorphisms of \(\mathbb F_2[x,y]/(x^2,y^2)\) and \(\mathbb F_4[x,y]/(x^2,y^2)\) by independently enumerating generator images and composing polynomials. Their idempotent image-dimension histograms are respectively \((1,12,1)\) and \((1,80,1)\) at dimensions \(1,2,4\). It also independently cross-checks the Gaussian-coefficient expression against the automorphism/stabilizer quotient for one hundred parameter cases, confirms the \(p=q=2,d=3\) histogram \((1,448,3584,1)\) algebraically, and evaluates three asymptotic concentration diagnostics in log space. Run using `python3 verify.py`. The finite computations do not establish the all-dimensional claims; the proof above does.

## Relationship to prior work
Chebolu, Corry, Grimm and Hatfield (2021) identify the truncated polynomial presentation of elementary-abelian modular group algebras and study their groups of units and ideal lattice, rather than enumerating algebra retractions. Balogh (2022) counts unitary subgroups of modular group algebras, a different invariant. Shpilrain and Yu (1997) discuss retracts of ordinary two-variable polynomial algebras in characteristic zero rather than the truncated finite-field family. A known low-dimensional enumeration of the four-dimensional characteristic-two exterior algebra supplies the \(p=2,d=2\) instance, which is explicitly not asserted as new. The contribution claimed here is the all-\(p,q,d\) retraction rank formula together with logarithmic-codimension concentration. Search and literature coverage do not amount to proof of publication priority.

## Limitations
All endomorphisms must preserve \(\mathbb F_q\) pointwise and preserve the identity; allowing nonunital or semilinear endomorphisms changes the counts. The asymptotic fixes \(p,q\); it makes no claim about simultaneous growth of the field. The exact orbit formula is a finite algebraic theorem, not a classification of group-algebra automorphisms as Hopf-algebra maps. An identical all-dimensional retract count or its asymptotic reformulation in older finite local-algebra literature may exist. No external independent audit has been performed.

## References
1. S. K. Chebolu, J. Corry, E. Grimm and A. Hatfield, Rings with an elementary abelian p-group of units, eprint 2112.03853 (2021).
2. Z. A. Balogh, The Order of the Unitary Subgroups of Group Algebras, eprint 2206.02113 (2022).
3. V. Shpilrain and J.-T. Yu, Polynomial Retracts and the Jacobian Conjecture (1997).
