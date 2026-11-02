# Exact negative-type threshold for generalized-quadrangle incidence metrics

## Finding
Let \(\mathcal Q\) be **any existing finite thick generalized quadrangle of order \((s,t)\)**, where \(s,t\) are integers at least \(2\). Write \(X\) for the union of its point and line sets and \(d\) for the ordinary unit-edge path metric of its point-line incidence graph. Put
\[
\begin{aligned}
A&=s(t+1)^2+t(s+1)^2,\\
B&=st\bigl(s(t+1)+t(s+1)\bigr),\\
C&=2st(s+1)(t+1),\qquad D=2(s+1)(t+1),\\
F_{s,t}(p)&=A2^p+B4^p-C3^p-D.
\end{aligned}
\]
There is exactly one positive real root \(\alpha_{s,t}\) of \(F_{s,t}(p)=0\), and
\[
0<\alpha_{s,t}<\log_2\left(1+\frac1{\max\{s,t\}}\right)<1.
\]
For every \(p\ge0\), the powered metric \(d^p\) has conditional negative type **if and only if** \(0\le p\le\alpha_{s,t}\). Equivalently, the kernel \(\exp(-\lambda d(x,y)^p)\) is positive semidefinite for every \(\lambda>0\) exactly on that interval. For each admissible \(p\) and fixed \(\lambda>0\), that kernel is actually strictly positive definite.

Writing \(N=(s+t+2)(st+1)\), the centered powered-distance form has no zero mode on the zero-sum subspace for \(0\le p<\alpha_{s,t}\), and has **exactly one** zero mode there at \(p=\alpha_{s,t}\). Thus the minimum squared-Euclidean embedding dimension for \(d^p\) is \(N-1\) below the endpoint and \(N-2\) at the endpoint. The endpoint null mode has a constant weight on every point and the opposite, separately normalized constant weight on every line. The classification depends only on \((s,t)\), not on the isomorphism class of the quadrangle.

In the smallest thick example of order \((2,2)\), \(\alpha_{2,2}=0.34578472347643\ldots\).

## Assumptions and scope
A finite generalized quadrangle of order \((s,t)\) is a point-line incidence structure in which each line contains \(s+1\) points, each point lies on \(t+1\) lines, any two points lie on at most one common line, and for every nonincident point-line pair there is exactly one point of the line collinear with the chosen point. We assume \(s,t\ge2\), with **existence** of the incidence structure; not every numerical parameter pair is asserted to exist. The incidence graph has \(P=(s+1)(st+1)\) point vertices and \(L=(t+1)(st+1)\) line vertices. Its path distances are \(1\) or \(3\) across the two parts; they are \(2\) or \(4\) between distinct vertices within one part. At \(p=0\), \(d(x,y)^0\) is defined to be \(1\) for distinct vertices and \(0\) on the diagonal.

For a real zero-sum vector \(z=(z_x)_{x\in X}\), conditional negative type means \(\sum_{x,y\in X}z_xz_y d(x,y)^p\le0\). The squared-Euclidean embedding dimension is the least integer \(m\) for which one can assign vectors \(v_x\in\mathbb R^m\) with \(\|v_x-v_y\|^2=d(x,y)^p\).

## Proof
**1. Incidence singular values.** Let \(M\) denote the \(P\)-by-\(L\) point-line incidence matrix and \(J\) an appropriately sized all-ones matrix. Set \(r=t+1\) and \(k=s+1\). The point-collinearity graph has strongly regular parameters
\[
\bigl((s+1)(st+1),\ s(t+1),\ s-1,\ t+1\bigr).
\]
Its adjacency matrix is \(MM^{\mathsf T}-rI\). The standard strongly regular identity \(A^2=(k_P-\mu)I+(\lambda-\mu)A+\mu J\), with \(k_P=s(t+1)\), \(\lambda=s-1\), \(\mu=t+1\), gives nonconstant eigenvalues \(s-1\) and \(-r\). Thus every nonzero singular value of \(M\) other than \(\sqrt{rk}\) equals \(\sqrt{s+t}\). The kernel of \(M^{\mathsf T}\) and the kernel of \(M\) account for the remaining singular-zero spaces. This uses only the quadrangle axioms.

**2. Powered-distance blocks.** Abbreviate \(a=2^p\), \(b=3^p\), \(c=4^p=a^2\). In the point/line decomposition, the distance-power matrix is exactly
\[
D_p=\begin{pmatrix}
 cJ+[t c-(t+1)a]I+(a-c)MM^{\mathsf T}&bJ-(b-1)M\\
 bJ-(b-1)M^{\mathsf T}&cJ+[s c-(s+1)a]I+(a-c)M^{\mathsf T}M
\end{pmatrix}.
\]
On the zero-sum subspace its orthogonal decomposition consists of (i) one contrast between the two constant parts; (ii) one-dimensional singular-zero sectors with scalar quadratic values \(a[t(a-1)-1]\) and \(a[s(a-1)-1]\); and (iii) paired singular-value sectors with symmetric two-by-two block
\[
T_p=\begin{pmatrix}
-a[1+s(a-1)]&-(b-1)\sqrt{s+t}\\
-(b-1)\sqrt{s+t}&-a[1+t(a-1)]
\end{pmatrix}.
\]
This decomposition requires neither vertex transitivity nor an automorphism group.

**3. Strict negativity of every noncontrast sector below a uniform bound.** For \(0\le p\le1\) put \(x=a-1\in[0,1]\). Convexity of \(u\mapsto u^{\gamma}\) on \([1,2]\), where \(\gamma=\log_2 3\in(1,2)\), gives \(b-1=a^{\gamma}-1\le2x\). Moreover \(a^2=(1+x)^2\ge4x\). Consequently
\[
\det T_p=a^2(1+sx)(1+tx)-(s+t)(b-1)^2
\ge a^2(1+stx^2)>0.
\]
Both diagonal entries of \(T_p\) are negative, so the block is strictly negative definite. The singular-zero sectors are strictly negative whenever
\[
0\le p<p_0:=\log_2\left(1+\frac1{\max\{s,t\}}\right).
\]
Thus **only the constant contrast can change sign** before \(p_0\).

**4. Exact constant-contrast equation.** Let \(z\) take value \(1/P\) on each point and \(-1/L\) on each line. It has sum zero. Every point has \(s(t+1)\) other collinear points and \(s^2t\) noncollinear points; every line meets \(t(s+1)\) other lines and is disjoint from \(st^2\) lines. A point is incident with \(t+1\) lines, and nonincident with \(st(t+1)\) lines. Counting these four distance types gives the **exact** identity
\[
z^{\mathsf T}D_p z=\frac{F_{s,t}(p)}{(s+1)(t+1)(st+1)}.
\]
In particular, \(F_{s,t}(0)=-(s+t+2)<0\). The positive and negative contributions of this one natural bipartition vector determine the entire threshold if its root precedes \(p_0\).

**5. Uniqueness and location of the root.** Let \(\gamma=\log_2 3\) and set \(u=2^p\ge1\). Write \(f(u)=Au+Bu^2-Cu^\gamma-D\). From the definitions,
\[
2B-C=2st(st-1)>0,
\]
while \(0<\gamma(\gamma-1)<1\). Hence
\[
f''(u)=2B-C\gamma(\gamma-1)u^{\gamma-2}>0\qquad(u\ge1).
\]
Since \(\gamma<8/5\),
\[
5f'(1)>5A+10B-8C
=4s^2t^2-s^2t-st^2+4st+5s+5t>0.
\]
Thus \(f\) is strictly increasing on \([1,\infty)\), starts negative, and tends to positive infinity; it has a unique positive-exponent root.

To locate it, use symmetry in \(s,t\) and suppose \(2\le s\le t\). The Taylor bound for \(1<\gamma<2\), together with \(\gamma<8/5\) and \(\gamma(\gamma-1)/2<1/2\), gives
\[
(1+x)^\gamma\le1+\frac85x+\frac12x^2\quad(x\ge0).
\]
Substituting \(x=1/t\) into \(f(1+x)\) therefore yields the explicit positive lower bound
\[
 f(1+1/t)\ge\frac{(s+1)(4s-5)(t+1)}5>0.
\]
Therefore \(0<\alpha_{s,t}<p_0<1\).

**6. Exhaustion, rank, and kernels.** At \(p=\alpha_{s,t}\) the constant contrast vanishes, while Steps 2--5 show every other zero-sum sector is strictly negative. This proves conditional negative type up to and including the root, with exactly one endpoint zero mode. For larger \(p\), strict increase of \(F_{s,t}\) makes the explicit contrast positive, proving failure. Schoenberg's finite-metric characterization equates conditional negative type with positive semidefiniteness of every \(\exp(-\lambda D_p)\). A finite squared-Euclidean embedding sends the distinct vertices to distinct points; Gaussian kernels on distinct Euclidean points are strictly positive definite. Finally the rank of the centered Gram matrix \(-\tfrac12 H D_pH\) is \(N-1\) below the root and \(N-2\) at the root, giving the claimed minimal embedding dimensions.

## Verification
The accompanying dependency-free `CHECK.py` verifies 4,213 independent assertion groups, including exact incidence axioms and all pair distances in the order-\((2,2)\) symplectic quadrangle, its numeric contrast-root sign transition, and symbolic-polynomial identity samples for all \(2\le s,t\le30\). Execute `python3 CHECK.py` in the same directory. The all-parameter statements are proven in Steps 1--6 rather than inferred from these finite checks. For instance the order-\((2,2)\) root is approximately \(0.34578472347643\).

## Relationship to prior work
Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (arXiv:1108.0451v1, publicly submitted 2011-08-02), develops a general distance-matrix criterion and computes the graph-metric exponent for complete bipartite graphs. Murugan, *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657v1, submitted 2011-12-23), analyzes row-transitive metrics and Hamming-cube subsets. Their inspected sections do not determine the generalized-quadrangle point-line incidence exponents, the strict contrast dominance, or the exceptional one-dimensional endpoint loss.

The incidence-geometry facts used here can be derived directly from the quadrangle axioms; they also appear in standard algebraic graph theory treatments. Earlier results for complete incidence designs and projective point-hyperplane graphs do not imply the present claim: generalized quadrangles include noncollinear point pairs, hence are not the corresponding \(2\)-design incidence structures, and their Levi graphs have diameter four rather than the projective graph's diameter three. The general finite-metric criterion alone does not provide the explicit closed two-parameter threshold or its unique controlling spectral sector.

## Limitations
The result is conditional on existence of a thick generalized quadrangle with the stated order and makes no claim classifying which \((s,t)\) occur. It does not classify other generalized polygons, variable edge lengths, or all individual eigenvalues of the positive-scale Gaussian kernel. The originality comparison is bounded by the inspected sources and research-record searches: an equivalent older association-scheme or generalized-polygon calculation may exist. No independent mathematical audit has been performed.

## References
1. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1 (2011-08-02), https://arxiv.org/html/1108.0451v1.
2. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (2011-12-23), https://arxiv.org/abs/1112.5657.
3. C. Godsil and G. Royle, *Algebraic Graph Theory*, Chapter 5, generalized quadrangles and incidence graphs (2001).
