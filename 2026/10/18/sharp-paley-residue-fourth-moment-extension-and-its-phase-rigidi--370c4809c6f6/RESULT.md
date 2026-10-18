# Sharp Paley-residue fourth-moment extension and its phase-rigidity threshold

## Finding
Let \(q\equiv3\pmod4\) be an odd prime power, let \(\mathbb F_q\) be its field, and put
\[
D=\{x^2:x\in\mathbb F_q^\times\},\qquad k=|D|=(q-1)/2.
\]
Fix a nontrivial additive character \(\psi\) and define, for \(f:D\to\mathbb C\),
\[
\mathcal E_Df(\xi)=\frac1k\sum_{x\in D}f(x)\psi(\xi x),\qquad \xi\in\mathbb F_q.
\]
With normalized counting measure on \(D\) and unnormalized counting measure on the frequency field, the **sharp** fourth-moment extension inequality is
\[
\boxed{\ \|\mathcal E_Df\|_{\ell^4(\mathbb F_q)}^4
\le \frac{q(q^2-2q+5)}{(q-1)^3}\|f\|_{L^2(D)}^4.\ }
\]
The complete classification of nonzero equality cases undergoes a sharp transition:

- For \(q=3\), every nonzero function (on the singleton \(D\)) is an extremizer.
- For \(q=7\), the extremizers are exactly the functions of constant nonzero modulus on \(D\), with **arbitrary** pointwise phases.
- For every \(q\ge11\) satisfying the stated hypotheses, the extremizers are exactly \(f(x)=c\psi(ax)\), where \(c\in\mathbb C^\times\) and \(a\in\mathbb F_q\). The parameter \(a\) is unique for each nonzero extremizer.

More strongly, the entire fourth-moment deficit has the **exact nonnegative decomposition** below. Put \(M=\sum_{x\in D}|f(x)|^2\), \(\lambda=(q-3)/4\), \(R=1+\lambda(1-1/k)\), and
\[
A_d=\sum_{x\in D\cap(D+d)}f(x)\overline{f(x-d)},\qquad
z_{d,x}=f(x)\overline{f(x-d)}.
\]
Then, for all complex \(f\),
\[
\boxed{\begin{aligned}
R M^2-\sum_{d\in\mathbb F_q}|A_d|^2
={}&\lambda\sum_{x\in D}\left(|f(x)|^2-\frac Mk\right)^2\\
&+\sum_{d\ne0}\ \sum_{\{x,y\}\subset D\cap(D+d)}
|z_{d,x}-z_{d,y}|^2.
\end{aligned}}
\]
The inner sum is over unordered **distinct** pairs. Every summand is nonnegative, and the identity is exact, not asymptotic. The first term detects amplitude imbalance; the second detects incompatibility of phase ratios along repeated differences.

## Assumptions and scope
The field has odd characteristic, cardinality congruent to \(3\) modulo \(4\), and the support is precisely the set of nonzero quadratic residues. All weights are complex; no flatness assumption is imposed on inputs. The source measure is \(k^{-1}\) times counting measure, and the target \(\ell^4\) uses counting measure. The assertion is a sharp \(L^2\)-to-\(\ell^4\) estimate and an equality/stability identity; it makes no assertion about other Fourier exponents, nonsquare residue classes, or fields with \(q\equiv1\pmod4\).

## Proof
**1. Difference-set geometry.** Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Since \(q\equiv3\pmod4\), \(\chi(-1)=-1\). For every \(d\ne0\), expansion of the indicator \(1_D(x)=(1+\chi(x)-1_{x=0})/2\), using
\[
\sum_x\chi(x)\chi(x-d)=-1,
\]
gives
\[
|D\cap(D+d)|=\frac{q-3}{4}=\lambda.
\]
Indeed, summing \((1+\chi(x))(1+\chi(x-d))\) over \(x\notin\{0,d\}\) yields \(q-3\), since the two truncated linear character sums cancel. Thus \(D\) is a \((q,k,\lambda)\) difference set in the additive field.

**2. An exact deficit.** Fourier orthogonality gives
\[
\sum_{\xi\in\mathbb F_q}\left|\sum_{x\in D}f(x)\psi(\xi x)\right|^4
=q\sum_{d\in\mathbb F_q}|A_d|^2.
\]
Write \(p_x=|f(x)|^2\). Here \(A_0=M\), and each ordered pair of distinct support points occurs exactly once among \((d,x)\) with \(d\ne0\) and \(x\in D\cap(D+d)\). For each nonzero \(d\), the elementary identity
\[
\lambda\sum_x|z_{d,x}|^2-\left|\sum_xz_{d,x}\right|^2
=\sum_{\{x,y\}}|z_{d,x}-z_{d,y}|^2
\]
therefore yields
\[
\sum_d|A_d|^2
=M^2+\lambda\left(M^2-\sum_xp_x^2\right)
-\sum_{d\ne0}\sum_{\{x,y\}}|z_{d,x}-z_{d,y}|^2.
\]
Since \(\sum_xp_x^2-M^2/k=\sum_x(p_x-M/k)^2\), rearrangement is exactly the displayed deficit identity. Consequently \(\sum_d|A_d|^2\le R M^2\), where \(R=(q^2-2q+5)/(4(q-1))\). Dividing the Fourier identity by \(k^4\), and noting \(\|f\|_{L^2(D)}^4=M^2/k^2\), gives the stated sharp constant \(qR/k^2=q(q^2-2q+5)/(q-1)^3\). Constant functions attain equality.

**3. Equality reduces to a restricted Freiman phase.** When \(q\ge7\), \(\lambda>0\), so equality for nonzero \(f\) forces \(p_x=M/k>0\) for every \(x\in D\), and forces the phase ratios \(u(x)\overline{u(x-d)}\) to be independent of \(x\in D\cap(D+d)\), with \(u(x)=f(x)/|f(x)|\). Denote their common value by \(c_d\), and set \(c_0=1\). Then \(c_{-d}=\overline{c_d}\). If every three distinct translates \(D,D+a,D+b\) have a common point, apply this condition to \(x,x-a,x-a-b\in D\). For \(a,b,a+b\ne0\), it gives \(c_{a+b}=c_a c_b\); the omitted cases follow from \(c_0=1\) and inversion. Hence \(d\mapsto c_d\) is an additive character. Because \(D-D=\mathbb F_q\), fixing one \(x_0\in D\) yields \(u(x)=u(x_0)c_{x-x_0}\) on all of \(D\), which is the restriction of an additive character up to scalar. Conversely, all these restrictions have constant modulus and perfectly aligned phase ratios, hence attain equality.

**4. The triple-intersection criterion holds uniformly from \(q=27\).** Let \(a,b\in\mathbb F_q\setminus\{0\}\) be distinct. Expanding the product of three terms \(1+\chi(x)\), \(1+\chi(x-a)\), and \(1+\chi(x-b)\) gives \(q-3+S\), where
\[
S=\sum_x\chi(x(x-a)(x-b)),\qquad |S|\le2\sqrt q.
\]
The last inequality is Hasse's bound for the elliptic curve with those three distinct roots; this is a standard external theorem used here, not a computation of an infinite set of cases. At the three excluded roots the product lies between \(0\) and \(4\), so removing them changes the sum by at most \(12\). Since a product at any remaining \(x\) is \(8\) exactly when all three translates contain \(x\), and is otherwise zero,
\[
|D\cap(D+a)\cap(D+b)|\ge\frac{q-15-2\sqrt q}{8}>0\qquad(q\ge27).
\]
This establishes the character-only equality cases for every admissible \(q\ge27\), including extension fields.

**5. The remaining prime fields.** The only admissible field orders below \(27\) are \(3,7,11,19,23\). For \(q=19\) and \(q=23\), exhaustive **integer** enumeration of all pairs of distinct nonzero shifts shows that the minimum triple-intersection count is exactly \(1\). The attached standalone checker implements that complete enumeration from the displayed square-residue definition, rather than extrapolating from samples. Thus the argument of step 3 applies to those two orders.

For \(q=11\), universal triple-intersection is false, so a different exact certificate is required. Here \(D=\{1,3,4,5,9\}\). Normalize \(u(1)=1\). The four genuine sum relations
\[
1+1=4+9,\quad 1+5=3+3,\quad 1+9=5+5,\quad3+4=9+9\pmod{11}
\]
force corresponding multiplicative equations on the phases. Their exponent matrix on the ordered variables \((u(3),u(4),u(5),u(9))\) is
\[
\begin{pmatrix}
0&-1&0&-1\\-2&0&1&0\\0&0&-2&1\\1&1&0&-2
\end{pmatrix},\qquad\det=-11.
\]
An integral square matrix of nonzero determinant \(m\) defines a covering homomorphism of the four-dimensional torus with kernel size \(|m|\); for example this follows from Smith normal form. Thus at most \(11\) normalized phase systems satisfy these four necessary equations. The \(11\) distinct normalized restricted characters \(u(x)=\psi(a(x-1))\), \(a\in\mathbb F_{11}\), all do satisfy them and all attain equality, so they exhaust the equality cases.

For \(q=7\), \(\lambda=1\), so every nonzero-difference fiber contains only one phase-ratio term; the second deficit term vanishes identically and the only restriction is constant modulus. At \(q=3\), \(k=1\) and the statement is immediate. The additive character parameter is unique for \(q\ge11\) because \(D-D=\mathbb F_q\). This completes the unrestricted proof.

## Verification
Run `python3 artifacts/verify.py` using the Python standard library. The checker reconstructs the residue sets and all nonzero-difference multiplicities for field orders \(3,7,11,19,23,27,31,43\), constructing \(\mathbb F_{27}\) as \(\mathbb F_3[T]/(T^3-T-1)\). It **exhaustively** checks the small-field triple intersections needed at orders \(19\) and \(23\), and independently calculates the order-\(11\) relation-matrix determinant as \(-11\). It also compares the Fourier fourth moments to the exact autocorrelation formula on \(96\) deterministic complex test inputs, covering \(1968\) frequency evaluations, verifies the deficit algebra and character extremizers, and checks the Hasse-derived threshold numerically. Its observed completion marker is `VERIFY_OK`. These numerical tests corroborate the identities; the all-field result rests on the complete proof, including the general elliptic-curve bound.

## Relationship to prior work
Iosevich and Koh (arXiv:0804.4505v1, first posted April 28, 2008) establish finite-field Fourier extension bounds for nondegenerate quadratic surfaces in ambient dimension at least two. Their sharp-dimensional methods motivate the problem, but their inspected results neither study the multiplicative quadratic-residue subset \(D\subset(\mathbb F_q,+)\) nor determine its extremizers or exact deficit. Bachoc, Matolcsi, and Ruzsa (2013) analyze quadratic residues as Paley graph configurations and address clique and difference-set bounds in a different arithmetic regime; those results do not imply this weighted fourth-moment phase-rigidity classification. Monico and Elia's additive characterizations of quadratic residues give a relevant historical representation-count perspective, not the asserted complex-weight equality geometry.

The classical Paley difference-set identity, the generic Cauchy–Schwarz bound for autocorrelations, the existence of additive characters, and Hasse's elliptic-curve character-sum bound are **not** claimed as new. The contribution is their precise combination into the exact sharp Fourier deficit and the complete \(q=7\) versus \(q\ge11\) phase-rigidity classification. Published finite-support fourth-moment and small-field sphere phase classifications were also compared; their objects and implications differ from the present all-field Paley-support result.

## Limitations
No independent priority certification or external mathematical audit has been performed. Some older work may encode related restricted-character rigidity using the language of partial difference sets or Freiman homomorphisms; this remains a genuine historical risk. The proof assumes the standard Hasse bound, and the two isolated orders \(19,23\) are discharged by exhaustive exact finite computation with the supplied source. The result is limited to \(q\equiv3\pmod4\), the quadratic-residue support, the fourth moment, and the stated normalization.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (first posted 2008-04-28).
2. C. Bachoc, M. Matolcsi, and I. Z. Ruzsa, *Squares and difference sets in finite fields*, 2013 (open manuscript at real.mtak.hu/7888).
3. C. Monico and S. Elia, *Note on an Additive Characterization of Quadratic Residues Modulo p*, historical open manuscript, 2006 draft (math.ttu.edu/~cmonico/research/qnr-charv5.pdf).
4. H. Hasse, the classical elliptic-curve point-count bound \(|\#E(\mathbb F_q)-(q+1)|\le2\sqrt q\); equivalently the quadratic-character estimate invoked in step 4.
