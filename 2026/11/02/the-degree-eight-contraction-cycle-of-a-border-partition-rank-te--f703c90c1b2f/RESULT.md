# The degree-eight contraction cycle of a border-partition-rank tensor

## Finding
For every integer \(n\geq5\), consider the four-way tensor \(T_n\) defined in Equation (7) and Theorem 4.11 of Baily–Danelon (2026), with its six bilinear placeholders specialized to the standard inner products on \(\mathbb C^n\). Its contraction-zero variety
\[
Z_n=\{(a,b,c)\in(\mathbb C^n)^3:T_n(a,b,c,d)=0\text{ for every }d\in\mathbb C^n\}
\]
has **exactly one irreducible component of maximal dimension**, and that component has dimension \(3n-3\), codimension \(3\), generic multiplicity \(1\), and projective degree **\(8\)**. In particular, the geometric rank of \(T_n\) is \(\operatorname{GR}(T_n)=3\) for every \(n\geq5\). The assertion about the component's degree concerns its projective closure in \(\mathbb P^{3n-1}\), with the standard homogeneous embedding.

Baily–Danelon's Theorem 4.11 establishes \(\operatorname{PR}(T_n)=4\) for all sufficiently large \(n\) and that \(T_n\) lies in the closure of tensors with partition rank at most \(3\). Thus, for sufficiently large \(n\), their rank-jump example additionally satisfies the strict separation \(\operatorname{GR}(T_n)=3<\operatorname{PR}(T_n)=4\), with an explicit degree-eight top-dimensional geometric cycle.

## Assumptions and scope
Work over \(\mathbb C\), with standard **bilinear**, not Hermitian, pairings \(u\cdot v=\sum_{i=1}^n u_i v_i\). For four variable vectors \(a,b,c,d\) let \(x^{(i)}\) be the first coordinate and \(y^{(i)}\) the second coordinate in the \(i\)-th vector. Set \(p_{ij}\) equal to the bilinear dot product of the \(i\)-th and \(j\)-th vectors. Explicitly,
\[
\begin{aligned}
T_n={}&p_{34}(x^{(1)}y^{(2)}-x^{(2)}y^{(1)})
+p_{24}(x^{(3)}y^{(1)}-x^{(1)}y^{(3)})\\
&+p_{14}(x^{(2)}y^{(3)}-x^{(3)}y^{(2)})\\
&+y^{(4)}(x^{(1)}p_{23}+x^{(2)}p_{13}+x^{(3)}p_{12})\\
&+x^{(4)}(y^{(1)}p_{23}+y^{(2)}p_{13}+y^{(3)}p_{12}).
\end{aligned}
\]
This is exactly the finite-coordinate substitution specified in the cited Theorem 4.11. Geometric rank means the codimension of the affine contraction-zero variety in the first three tensor factors. A component of \(Z_n\) is **top-dimensional** if its dimension is maximal among all irreducible components; possible smaller components are not classified by this theorem.

## Proof
**1. Exact contraction equations.** Define the first and second coordinate rows and remaining rows by
\[
\alpha=(a_1,b_1,c_1),\quad\beta=(a_2,b_2,c_2),\quad\gamma_j=(a_j,b_j,c_j)\quad(3\leq j\leq n),
\]
and the quadratic vector
\[
q=(b\cdot c,\ a\cdot c,\ a\cdot b).
\]
Expanding the source's tensor in the fourth vector gives the identity
\[
T_n(a,b,c,d)=d_1(\beta\cdot q)+d_2(\alpha\cdot q)
+\sum_{j=3}^{n}d_j\det\begin{pmatrix}\alpha\\\beta\\\gamma_j\end{pmatrix}.
\]
Hence \(Z_n\) is cut out set-theoretically by the two cubic equations \(\alpha\cdot q=\beta\cdot q=0\) and the \(n-2\) cubic minors \(\det(\alpha,\beta,\gamma_j)=0\).

**2. Rank-one stratum.** Let \(R\) be the determinantal variety \(\operatorname{rank}\binom{\alpha}{\beta}\leq1\), with the other \(3(n-2)\) coordinates arbitrary. It is irreducible of dimension \(3n-2\), codimension \(2\), and projective degree \(3\): the nontrivial factor is the cone over the Segre \(\mathbb P^1\times\mathbb P^2\), whose degree is \(\binom31=3\).

On the dense parameter domain write \(\alpha=s v\), \(\beta=t v\) with \(v=(v_1,v_2,v_3)\ne0\) and \((s,t)\ne(0,0)\), modulo \((s,t,v)\sim(\lambda^{-1}s,\lambda^{-1}t,\lambda v)\). The three components of each \(\gamma_j\) are free, and the contraction equations become \(sF=tF=0\), where
\[
F=3(s^2+t^2)v_1v_2v_3+
\sum_{j=3}^{n}\bigl(v_1\gamma_{j2}\gamma_{j3}
+v_2\gamma_{j1}\gamma_{j3}
+v_3\gamma_{j1}\gamma_{j2}\bigr).
\]
The determinant equations vanish on \(R\). Because \((s,t)\ne(0,0)\), the desired intersection on that dense domain is exactly \(F=0\).

**3. Irreducibility.** In the polynomial ring in \(s,t,v,\gamma_3,\ldots,\gamma_n\), regard \(F\) as linear in \(\gamma_{3,1}\). The coefficient is
\(L=v_2\gamma_{3,3}+v_3\gamma_{3,2}\), an irreducible polynomial. Its constant term \(C\) is not divisible by \(L\): for example, specialize \(s=1,t=0\), \(v=(1,1,0)\), \(\gamma_3=0\), \(\gamma_4=(0,1,1)\), and all later rows to zero. This makes \(L=0\) while \(C=1\). Thus \(\gcd(L,C)=1\), and the primitive degree-one polynomial \(L\gamma_{3,1}+C\) is irreducible by Gauss's lemma. The hypothesis \(n\geq5\) ensures the independent row \(\gamma_4\) is available. Consequently the closure \(W_n\) of \(\{\operatorname{rank}(\alpha,\beta)=1,F=0\}\) inside \(R\) is irreducible. It has dimension
\[
(2+3+3(n-2))-1_{\mathrm{scaling}}-1_{\mathrm{equation}}=3n-3,
\]
and therefore codimension \(3\) in \(\mathbb A^{3n}\).

**4. No other maximal components.** On the open set where \(\alpha,\beta\) are linearly independent, all determinant equations force \(\gamma_j\in\operatorname{span}(\alpha,\beta)\), giving an irreducible locus of codimension \(n-2\) in \(\mathbb A^{3n}\). The additional cubic \(\alpha\cdot q\) is not identically zero there: choose \(\alpha=(1,1,1)\), \(\beta=(1,0,0)\), and every \(\gamma_j=0\), for which \(\alpha\cdot q=3\). Thus the contraction-zero locus on the independent-row stratum has codimension at least \(n-1\geq4\). On \(R\), the rank-one locus is dense and its complement \(\alpha=\beta=0\) has codimension \(4\) in \(R\). Hence all components supported in that complement have codimension \(6\) in ambient space. It follows that \(W_n\) is the **unique** codimension-three component, proving the geometric-rank statement.

**5. Degree and multiplicity.** In the projective coordinate ring of the integral determinantal variety \(R\), the homogeneous cubic \(U=\alpha\cdot q\) is a nonzerodivisor (it is nonzero generically, for example at \(\alpha=(1,1,1),\beta=0,\gamma_3=(0,1,1)\)). Consequently the cubic hypersurface section \(R\cap V(U)\) has total effective projective cycle degree \(3\deg R=9\). On the rank-one parameterization \(U=sF\). Its only codimension-one components are \(W_n\) and the linear space \(D_\alpha=\{\alpha=0\}\), each generically of multiplicity \(1\) since \(F\) is irreducible, and \(F\) is nonzero generically along \(s=0\). For instance \(s=0,t=1,v=(1,1,1)\), with all \(\gamma_j=0\), gives \(F=3\). The singular vertex \(\alpha=\beta=0\) has codimension four in \(R\) and introduces no divisorial component. Since \(D_\alpha\) is linear of degree \(1\), comparison of effective projective cycles gives
\[
9=\deg W_n+\deg D_\alpha=\deg W_n+1,
\qquad\boxed{\deg W_n=8}.
\]
The factorization \(sF\) also establishes multiplicity one for the component \(W_n\) of the contraction-zero equations: on its dense rank-one stratum the row-minor equations are transverse in the normal directions to \(R\), and \(sF,tF\) generate the reduced divisor equation \(F\) there. This completes the proof. \(\square\)

## Verification
The included `verify.py` is a standalone Python 3 script using exact integer arithmetic. It checks the four-way source formula against the displayed contraction coefficients on deterministic parameter samples, checks the rank-one substitution, and recomputes the Segre cubic-section degree calculation. Run `python3 verify.py` and expect `VERIFY_OK`. These finite checks test normalizations but do not substitute for the irreducibility, dimension, or intersection-cycle arguments above.

## Relationship to prior work
Baily and Danelon, *Closedness of bounded strength and partition rank loci* (arXiv:2610.28792v1), Equation (7), Proposition 4.10 and Theorem 4.11, construct this tensor and establish eventual partition rank four and border partition rank at most three. Their result does **not** state this tensor's geometric rank or the degree of its contraction-zero top cycle. Kopparty–Moshkovitz–Zuiddam (arXiv:2002.09472) introduce geometric rank, and Geng (arXiv:2201.03615) studies general geometric rank and tensor varieties; neither addresses the particular four-way tensor family and cycle. A prior equivalent contraction calculation under a change of tensor coordinates remains possible and would affect historical novelty.

## Limitations
All statements concern the given complex four-way tensor and its contraction variety, not arbitrary tensors of partition or border partition rank three. The threshold for actual partition rank four is the unspecified sufficiently-large threshold established by the cited source, not asserted to equal five here. We do not classify components of dimension below \(3n-3\), nor their embedded scheme structures. Generic multiplicity one is proved only for the unique top-dimensional component. No independent external validation or definitive priority certification is claimed.

## References
1. Benjamin Baily and Alessandro Danelon, *Closedness of bounded strength and partition rank loci*, arXiv:2610.28792v1 (20 October 2026), Equation (7), Proposition 4.10 and Theorem 4.11. https://arxiv.org/html/2610.28792v1
2. Swastik Kopparty, Guy Moshkovitz and Jeroen Zuiddam, *Geometric rank of tensors and subrank of matrix multiplication*, arXiv:2002.09472 (2020; revised 2023). https://arxiv.org/abs/2002.09472
3. Runshi Geng, *Geometric rank and linear spaces of matrices of bounded rank*, arXiv:2201.03615 (2022). https://arxiv.org/abs/2201.03615
