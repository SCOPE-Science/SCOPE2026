# Jordan-type transfer matrix for the radical of a linear truncated path algebra

## Finding
For every integer \(n\ge 3\) and finite field \(k=\mathbb F_q\), consider the linearly oriented quiver \(Q_n:1\to2\to\cdots\to n\), its path algebra \(A_n=kQ_n/J^3\), and its Jacobson radical \(J\). Define \(L_x:A_n\to A_n\) by \(L_x(y)=xy\) for \(x\in J\). Let \(r(x)=\operatorname{rank}_k L_x\) and \(s(x)=\operatorname{rank}_k L_x^2\). Write \(c=q-1\). The complete joint distribution is
\[
\boxed{\sum_{x\in J}X^{r(x)}Y^{s(x)}=(1,cX^2)M^{n-3}F\binom11},
\]
where
\[
M=\begin{pmatrix}1+cX&qcX^2\\q&qcX^2Y\end{pmatrix},\qquad
F=\begin{pmatrix}1+cX&qcX\\q&qcXY\end{pmatrix}.
\]
The left side consequently determines the complete nilpotent Jordan partition of every left multiplication map, including the multiplicity of each partition. The boundary cases are \(T_1(X,Y)=1\) and \(T_2(X,Y)=1+(q-1)X\).

The number of square-zero radical elements is exactly
\[
\boxed{\#\{x\in J:x^2=0\}=q^{n-2}\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-j}{j}(q-1)^j}\quad(n\ge2).
\]

## Assumptions and scope
The coefficient field is any finite field of prime-power order \(q\). Paths are multiplied by concatenation when endpoints agree and vanish if total length is at least three. For \(n\ge2\), \(A_n\) has the basis of \(n\) trivial paths \(e_i\), \(n-1\) arrows \(u_i\), and \(n-2\) length-two paths \(v_i=u_i u_{i+1}\); hence \(\dim_k A_n=3n-3\). Any radical element has a unique expansion
\[
x=\sum_{i=1}^{n-1}a_i u_i+\sum_{i=1}^{n-2}b_i v_i.
\]
For \(1\le i\le n-1\), let \(\epsilon_i=1\) when \(a_i\ne0\), and \(\epsilon_i=0\) otherwise. Let \(\eta_i=1\) when \(b_i\ne0\). Exponents in the generating polynomial count dimensions over \(k\), not algebraic rank of \(x\) as an element.

## Proof
The basis gives, with out-of-range coefficients interpreted as zero, \(L_xe_{i+1}=a_i u_i+b_{i-1}v_{i-1}\), \(L_xu_{i+1}=a_i v_i\), and \(L_xv_i=0\). For the squared operator, \(L_x^2e_{i+2}=a_i a_{i+1}v_i\), and all other possible images vanish.

The nonzero arrow coordinates \(a_i u_i\) in the images of the trivial paths are independent and contribute exactly \(\sum_i\epsilon_i\) to \(\operatorname{rank}L_x\). The \(v_i\)-direction is already available independently when \(a_i\ne0\), via \(L_xu_{i+1}\). If \(a_i=0\), the \(v_i\)-coordinate in \(L_xe_{i+2}\) is \(b_i\). When \(a_{i+1}\ne0\), that column has an indispensable new \(u_{i+1}\)-coordinate, so the coefficient \(b_i\) cannot add a dimension. When both adjacent arrow coefficients vanish, the nonzero \(b_i\) supplies a new independent pure \(v_i\)-direction. This triangular-support argument gives the exact identities
\[
\boxed{r(x)=\sum_{i=1}^{n-1}\epsilon_i+\sum_{i=1}^{n-2}\epsilon_i+\sum_{i=1}^{n-2}(1-\epsilon_i)(1-\epsilon_{i+1})\eta_i},
\qquad
\boxed{s(x)=\sum_{i=1}^{n-2}\epsilon_i\epsilon_{i+1}}.
\]
The second equality also follows immediately because the displayed images of \(L_x^2\) occupy distinct length-two path directions.

Fix the binary support pattern of the arrow coefficients. A zero arrow coefficient has one realization; a nonzero coefficient has \(c\) realizations. For an adjacent pair of arrow-support states \(e,f\in\{0,1\}\), the intervening length-two coefficient has \(q\) arbitrary choices when \(e+f>0\), contributing no additional operator rank, whereas when \(e=f=0\) it has one zero choice of rank increment zero and \(c\) nonzero choices of rank increment one, giving factor \(1+cX\). An adjacent pair with \(e=f=1\) adds one to \(s\), contributing \(Y\). Each new nonzero arrow contributes \(2\) to \(r\) unless it is the final arrow, which contributes \(1\). The first arrow contributes \(2\) when nonzero, so the initial row is \((1,cX^2)\). Each interior transition therefore has matrix \(M\) as displayed; the final transition has matrix \(F\). Multiplying the initial vector by \(n-3\) interior transitions and then one final transition, and summing over the final support state, proves the generating-polynomial identity.

Since \(J^3=0\), each \(L_x\) is nilpotent of order at most three. In its Jordan decomposition, each size-three block contributes \(2\) to \(r\) and \(1\) to \(s\); each size-two block contributes \(1\) to \(r\) and none to \(s\). Thus when \(D=3n-3\), the numbers of blocks of sizes three, two, and one are respectively \(s\), \(r-2s\), and \(D-2r+s\). This reconstructs a unique partition from each coefficient of the joint polynomial.

Finally, \(x^2=\sum_i a_i a_{i+1}v_i\). Thus \(x^2=0\) exactly when the set of nonzero arrow positions is an independent set in a path on \(n-1\) vertices. An independent set of size \(j\) can be chosen in \(\binom{n-j}{j}\) ways, and its nonzero arrow coefficients in \(c^j\) ways. All \(n-2\) length-two coefficients are free, accounting for \(q^{n-2}\). This proves the second formula. The boundary cases follow directly from the one-arrow or empty-arrow basis.

## Verification
The accompanying self-contained `verify.py` constructs the complete left-regular matrix in the path basis, computes its rank and the rank of its square by finite-field elimination, and compares each pair of ranks with two independent support-based enumerations. Exhaustive tests cover field sizes \(2,3,5\) and every tested quiver size up to seven subject to the recorded search-size cap; the program prints `VERIFY_OK_REGULAR_NAKAYAMA_JORDAN` when successful. The proof does not rely on these finite computations.

## Relationship to prior work
Xu, Han and Jiang study Hochschild cohomology of truncated quiver algebras over arbitrary characteristics. Their full available text defines the same broad class, but its stated theorems compute Hochschild cohomology and global-dimension conditions, not distributions of Jordan types of the left-regular action of individual radical elements. Dugas, Huisgen-Zimmermann and Learned study the homological structure and syzygies of truncated path algebras. Their accessible abstract does not settle the operator-Jordan distribution studied here; their complete article was not inspected, so this comparison carries residual risk. Babson, Huisgen-Zimmermann and Thomas address generic representation families, likewise a different invariant; only the abstract was available here. Classical path bases, nilpotence, and independent-set enumeration are not asserted to be new. The proposed contribution is their exact synthesis into an all-rank, all-field Jordan-type transfer matrix for the regular module.

## Limitations
The enumeration is for elements of the radical, and for multiplication on the full regular module; it is not an automorphism-orbit classification, not a census of modules, and not a theorem for arbitrary orientations or longer truncation lengths. For \(n=1\), the radical is zero. Exhaustive calculations are finite corroboration only. Historical priority may be affected by equivalent formulas hidden in the uninspected full text of relevant representation-theoretic literature. Independent mathematical auditing has not been performed.

## References
- Y. Xu, Y. Han and W. Jiang, *Hochschild cohomology of truncated quiver algebras* (public preprint, 9 September 2005), arXiv:math/0509202v1, https://arxiv.org/abs/math/0509202.
- A. Dugas, B. Huisgen-Zimmermann and J. Learned, *Truncated path algebras are homologically transparent* (public preprint, 10 July 2014), arXiv:1407.2672v1, https://arxiv.org/abs/1407.2672.
- E. Babson, B. Huisgen-Zimmermann and R. Thomas, *Generic representation theory of quivers with relations* (public preprint, 10 July 2014), arXiv:1407.2673v1, https://arxiv.org/abs/1407.2673.
