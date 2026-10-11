# Sharp fourth-moment Fourier extension for even-degree Gold graphs and quadratic-sign extremizers

## Finding
For every integer \(m\ge1\), let \(q=4^m\) and \(K=\mathbb F_q\). Define the graph \(C=\{(x,x^5):x\in K\}\). For any nontrivial additive character \(\psi:K\to\mathbb C\) and any \(f:K\to\mathbb C\), put
\[
\mathcal E f(u,v)=q^{-1}\sum_{x\in K} f(x)\psi(ux+vx^5).
\]
Then the sharp inequality, with counting measure on the target and normalized counting measure on the source, is
\[
\boxed{\sum_{u,v\in K}|\mathcal E f(u,v)|^4\le\left(5-\frac4q\right)\left(q^{-1}\sum_{x\in K}|f(x)|^2\right)^2.}
\]
Choose any \(\mathbb F_4\)-linear coordinates \(x\leftrightarrow(z_1,\ldots,z_m)\in\mathbb F_4^m\). Every nonzero equality case, and only such a case, has the form
\[
\boxed{f(x)=\lambda(-1)^{h(x)},\quad h(x)=\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}\left(\sum_i b_i z_i+\sum_{i<j}a_{ij}z_i z_j\right),}
\]
where \(\lambda\in\mathbb C\setminus\{0\}\) and \(a_{ij},b_i\in\mathbb F_4\) are arbitrary. There are exactly \(2^{m^2+m}\) such maximizers modulo multiplication by nonzero complex scalars; the classification is independent of the coordinate choice.

## Assumptions and scope
The field \(K\) has characteristic two and dimension \(2m\) over \(\mathbb F_2\). It contains its unique subfield \(\mathbb F_4\), and \(\omega\in\mathbb F_4\setminus\mathbb F_2\) denotes a root of \(\omega^2+\omega+1=0\). The trace \(\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(z)=z+z^2\) is used only for the sign description, not for the chosen additive character. The zero signal satisfies the inequality but is not counted as an extremizer. No assertion is made here for odd extension degree or other powers.

## Proof
**1. Exact fourth-moment/fiber identity.** Define \(S=\sum_x|f(x)|^2\) and, for \(s,t\in K\),
\[
A_{s,t}=\sum_{\substack{x,y\in K\\x+y=s,\ x^5+y^5=t}}f(x)f(y).
\]
Character orthogonality on \(K^2\) yields the exact formula
\[
q^2\sum_{u,v\in K}|\mathcal E f(u,v)|^4=\sum_{s,t\in K}|A_{s,t}|^2=:T.
\]
Every pair with \(s=0\) has \(x=y\) in characteristic two, so \(A_{0,0}=\sum_x f(x)^2\) and every other \(A_{0,t}\) vanishes.

**2. Uniform four-element differential fibers.** For fixed \(s\ne0\), let \(D_s(x)=x^5+(x+s)^5\). The binomial identity in characteristic two gives
\[
D_s(su)=s^5(1+u+u^4).
\]
The linearized map \(u\mapsto u^4+u\) has kernel precisely \(\mathbb F_4\), hence each nonempty fiber of \(D_s\) has four elements, a coset of \(s\mathbb F_4\). Consequently,
\[
T=\left|\sum_xf(x)^2\right|^2+\sum_{s\ne0}\sum_{t\in K}\left|\sum_{x:D_s(x)=t}f(x)f(x+s)\right|^2.
\]

**3. Sharp bound and equality at the amplitude level.** By four-term Cauchy–Schwarz on every nonempty differential fiber,
\[
\sum_t\left|\sum_{x:D_s(x)=t}f(x)f(x+s)\right|^2
\le4\sum_x|f(x)|^2|f(x+s)|^2.
\]
Moreover \(\big|\sum_x f(x)^2\big|^2\le S^2\). Summing over nonzero \(s\) gives
\[
T\le S^2+4\left(S^2-\sum_x|f(x)|^4\right)
\le\left(5-\frac4q\right)S^2.
\]
The last step uses \(\sum_x|f(x)|^4\ge S^2/q\). If \(f\ne0\), equality forces equal nonzero amplitudes at all field points and equality in the triangle inequality for \(\sum_x f(x)^2\). Therefore \(f(x)=\lambda\varepsilon(x)\) for a fixed \(\lambda\ne0\) and \(\varepsilon(x)\in\{\pm1\}\). These conditions are sufficient for the first and last inequalities.

**4. Phase equality becomes a line-parity code.** Equality in each four-term Cauchy–Schwarz step means that the four products \(\varepsilon(x)\varepsilon(x+s)\) are equal for \(x\) in a given coset of \(s\mathbb F_4\). Because translation by \(s\) pairs the four points into two pairs, this is equivalent to
\[
\prod_{y\in(x+s\mathbb F_4)}\varepsilon(y)=1.
\]
Write \(\varepsilon(x)=(-1)^{h(x)}\) with \(h:K\to\mathbb F_2\). Equality is thus equivalent to the zero-line-sum condition
\[
\boxed{\sum_{u\in\mathbb F_4}h(x+us)=0\quad\text{in }\mathbb F_2\qquad(x\in K,\ s\in K^\times).}
\]
It suffices to classify these sign functions; all such signs attain the bound because each inequality above is then an equality.

**5. Line-parity classification by induction.** Identify \(K\) as the \(\mathbb F_4\)-space \(\mathbb F_4^m\). Let \(\mathcal L_m\) denote the \(\mathbb F_2\)-space of functions with zero sum on every affine \(\mathbb F_4\)-line, and let \(\mathcal L_0\) be all functions on a singleton. Fix the final coordinate \(z\in\mathbb F_4\) and write \(x\in\mathbb F_4^{m-1}\). The vertical-line condition is exactly the statement that, uniquely,
\[
h(x,z)=h_0(x)+\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(a(x)z),
\]
for \(h_0:\mathbb F_4^{m-1}\to\mathbb F_2\) and \(a:\mathbb F_4^{m-1}\to\mathbb F_4\). Horizontal lines show \(h_0\in\mathcal L_{m-1}\) and, by nondegeneracy of the trace pairing,
\[
\sum_{u\in\mathbb F_4}a(x+us)=0\quad\text{for every }x,s.
\]
A mixed line with direction \((s,t)\) and arbitrary \(t\in\mathbb F_4\) then shows
\[
\sum_{u\in\mathbb F_4}u\,a(x+us)=0\quad\text{for every }x,s.
\]
For a function of \(u\in\mathbb F_4\), write its unique degree-at-most-three polynomial as \(c_0+c_1u+c_2u^2+c_3u^3\). The two displayed sums vanish exactly when \(c_3=c_2=0\), since \(\sum_{u\in\mathbb F_4}u^3=1\) and \(\sum u^k=0\) for \(k=0,1,2,4\). Hence \(a\) is \(\mathbb F_4\)-affine on every \(\mathbb F_4\)-line.

To show that \(a\) is globally \(\mathbb F_4\)-affine, use its coordinate-wise affine property to express it uniquely as a multiaffine polynomial in the \(m-1\) variables. Varying any two coordinates jointly along a line, the coefficient of \(u^2\) is the mixed two-coordinate coefficient polynomial. Since restriction to every line is affine in \(u\), all such coefficients vanish at every value of the other variables. Thus every multiaffine monomial of degree at least two disappears and \(a(x)=b_m+\sum_{i<m}a_{im}z_i\).

Conversely, every \(h_0\in\mathcal L_{m-1}\) and every globally \(\mathbb F_4\)-affine \(a\) yields a function in \(\mathcal L_m\): on an arbitrary line the added trace term is the trace of a polynomial of degree at most two in \(u\), whose four-value sum vanishes. Inducting from \(\mathcal L_0=\mathbb F_2\) gives precisely
\[
h(z)=c+\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}\left(\sum_i b_i z_i+\sum_{i<j}a_{ij}z_i z_j\right),
\]
with \(c\in\mathbb F_2\). Its parameter space has dimension
\[
1+2m+2\binom m2=m^2+m+1\quad\text{over }\mathbb F_2.
\]
Absorbing the constant sign \((-1)^c\) into \(\lambda\) proves the announced equality form and the number \(2^{m^2+m}\) of projective maximizers. For \(m\ge2\), choosing a nonzero mixed quadratic coefficient gives a genuinely non-character extremizer.

## Verification
The accompanying standalone `gold_checker.py` reconstructs exact binary extension fields using specified irreducible polynomials, directly computes the convolution fiber energy for arbitrary complex inputs, and checks the sharp bound and explicit quadratic-sign equality functions. It computes the binary ranks of the affine \(\mathbb F_4\)-line incidence constraints for \(q=4,16,64,256\), finding nullities \(3,7,13,21\), respectively, in agreement with \(m^2+m+1\). It exhaustively checks the \(16\) and \(65{,}536\) sign patterns for \(q=4,16\), finding \(8\) and \(128\) sign patterns satisfying every line constraint. It additionally passes \(66\) direct complex-energy tests and optimizer tests across these four fields. All infinite-dimensional and all-field assertions rest on the proof above, not on finite computation.

## Relationship to prior work
Finite-field polynomial-graph restriction estimates supply exponent ranges but not this numerical sharp constant with the complete equality classification. Work on Gold powers describes differential uniformity and related substitution-box constructions; the four-element derivative fibers used here are classical algebra. Sharp finite-field \(L^2\to L^4\) extensions of quadratic hypersurfaces address different supports. General fourth-Walsh-moment characterizations of differential uniformity concern the constant input rather than arbitrary weighted input and the full projective optimizer family. The result here combines the weighted extension inequality with an exact affine-subfield line-code classification.

## Limitations
The theorem covers the Gold fifth-power graph only when the binary extension degree is even. The equivalence-class count is for maximizers modulo nonzero complex scaling, not for distinct raw functions, and depends on the input normalization above. The line-code characterization may have equivalent forms in older incidence-coding literature; no universal priority claim is made.

## References
- H. Yan, S. Mesnager, Z. Zhou, *Power Functions over Finite Fields with Low c-Differential Uniformity*, arXiv:2003.13019v1 (first public 2020-03-29), particularly Section III on Gold exponents.
- L. Budaghyan, M. Calderini, C. Carlet, R. Coulter, I. Villa, *Generalized isotopic shift construction for APN functions*, Designs, Codes and Cryptography (2020 online), DOI:10.1007/s10623-020-00803-1, especially Section 2, Remark 2.1.
- D. Koh, C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, Rev. Mat. Iberoam. 28 (2012), 157–178, DOI:10.4171/RMI/672.
- C. Carlet, *Componentwise APNness, Walsh uniformity of APN functions and cyclic-additive difference sets*, IACR ePrint 2017/528.
- C. González-Riquelme, D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647.
