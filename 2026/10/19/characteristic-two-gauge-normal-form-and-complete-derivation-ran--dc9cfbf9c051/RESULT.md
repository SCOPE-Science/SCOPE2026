# Characteristic-two gauge normal form and complete derivation-rank spectrum of model filiform Lie algebras

## Finding

Let \(k=\mathbb F_q\) be any finite field of characteristic two, let \(n\ge4\), and let \(L_n\) be the \(n\)-dimensional model filiform Lie algebra with basis \(e_1,\ldots,e_n\), alternating bracket, and the only nonzero basic brackets \([e_1,e_j]=e_{j+1}\) for \(2\le j<n\). Set \(d=n-1\), \(h=\lceil d/2\rceil\), and \(b=\lfloor d/2\rfloor\). For any positive integer \(\ell\le d\) define
\[
W_\ell(j)=\begin{cases}
(q-1)q^{d-1-j},&1\le j<\ell,\\
q^{d-\ell},&j=\ell,\\
0,&\text{otherwise}.
\end{cases}
\]
The rank-generating polynomial of **all** linear derivations is
\[
\boxed{\begin{aligned}
\mathcal P_{n,q}(z)&=\sum_{D\in\operatorname{Der}_k(L_n)}z^{\operatorname{rank}_k D}\\
&=1+(q^d-1)z\\
&\quad+\sum_{r=1}^{d}(q-1)q^{r-1}\bigl(q^r z^r+(q^d-q^r)z^{r+1}\bigr)\\
&\quad+(q-1)(q-2)q^{2d-1}z^n\\
&\quad+(q-1)q^d\left(\sum_{j=1}^{h}W_h(j)z^{n-j}
+\sum_{j=1}^{b}W_b(j)z^{n-j}\right).
\end{aligned}}
\]
In particular, \(\mathcal P_{n,q}(1)=q^{2n-1}\), every derivation is singular over \(\mathbb F_2\), and, for every \(q>2\), the exact fraction of nonsingular derivations is
\[
\boxed{\frac{\#\{D\in\operatorname{Der}_k(L_n):\det D\ne0\}}{\#\operatorname{Der}_k(L_n)}=\frac{(q-1)(q-2)}{q^2}.}
\]
The fraction is independent of the dimension, although the other rank multiplicities vary with the parity of \(n-1\).

## Assumptions and scope

The Lie bracket is alternating even in characteristic two; equivalently, \([x,x]=0\) for every \(x\). The rank is that of the underlying \(k\)-linear transformation, not the adjoint rank \(\operatorname{rank}(\operatorname{ad}_x)\). No restriction to inner, homogeneous, invertible, or semisimple derivations is made. Finite fields have orders \(q=2^f\) with integer \(f\ge1\). The assertion covers every \(n\ge4\); the exceptional small dimensions are not asserted to satisfy this normal form.

Let \(V=\langle e_2,\ldots,e_n\rangle\), identify it with \(R=k[t]/(t^d)\) by \(e_{j+2}\leftrightarrow t^j\), and write \(E=t\frac{d}{dt}\) on \(R\). Write \(M_w\) for multiplication by \(w\in R\).

## Proof

**1. All derivations.** For any derivation \(D\), write \(D(e_1)=a e_1+v\) with \(a\in k\) and \(v\in V\). The \(e_1\)-coefficient of \(D(e_2)\) must vanish: apply \(D\) to \([e_2,e_3]=0\); its possible \(e_4\)-coefficient is precisely that coefficient. Here \(e_4\) exists because \(n\ge4\). Thus \(D(e_2)=w\in V\). Applying \(D\) successively to \(e_{j+1}=[e_1,e_j]\) forces
\[
D(e_{j+1})=a e_{j+1}+[e_1,D(e_j)]\qquad(2\le j<n).
\]
The remaining zero brackets impose no further constraints, since \(D(V)\subseteq V\) and \([V,V]=0\). Under the polynomial identification this gives exactly
\[
D=\begin{pmatrix}a&0\\v&aE+M_w\end{pmatrix},
\qquad a\in k,\quad v,w\in R,
\]
with no repetitions. Therefore the derivation space has \(q^{2d+1}=q^{2n-1}\) elements. If \(a\ne0\), the elementary column operation on the initial basis column shows \(\operatorname{rank}D=1+\operatorname{rank}(aE+M_w)\). If \(a=0\), its image is \(k v+\operatorname{im}M_w\).

**2. The stratum \(a=0\).** If \(w=0\), there is one rank-zero derivation (\(v=0\)) and \(q^d-1\) rank-one derivations. If \(w\ne0\) has truncated \(t\)-valuation \(d-r\), then \(M_w\) has rank \(r\), and there are \((q-1)q^{r-1}\) choices of \(w\) for each \(1\le r\le d\). There are exactly \(q^r\) choices of \(v\) in its image; those yield rank \(r\), while the remaining \(q^d-q^r\) choices yield rank \(r+1\). This proves the first line and the sum indexed by \(r\) in the stated formula.

**3. Characteristic-two gauge lemma.** For \(a\ne0\), normalize \(f=w/a\). Every formal power series \(f\in k[[t]]\) admits a unique parity splitting \(f=f_0(s)+t f_1(s)\) with \(s=t^2\). There is a unique \(z\in k[[s]]\) satisfying
\[
z+s f_1 z^2=f_1.
\]
Indeed, the constant coefficient of \(z\) is that of \(f_1\); each coefficient of \(s^i\) on the right involving \(s f_1 z^2\) uses coefficients of \(z\) of strictly lower degree. This recursive argument makes no separability or algebraic-closure assumption. Define \(u=1+t z(s)\), a unit, and \(h(s)=f_0(s)+s f_1(s)z(s)\). Since the characteristic is two, \(E(z(s))=0\) and \(E(u)=tz(s)\). Expanding and using the defining equation for \(z\) gives
\[
(E+M_f)(u)=u h(s),\qquad
M_u^{-1}(E+M_f)M_u=E+M_{h(t^2)}.
\]
These equalities hold in the formal power-series ring, hence in every quotient \(k[t]/(t^d)\), including boundary truncations. Crucially, for fixed odd part \(f_1\) the map \(f_0\mapsto h\) is a translation; no even coefficient distribution is distorted by gauge normalization.

**4. Counting the two resonance strata.** On \(R\), the even-power subspace has dimension \(h=\lceil d/2\rceil\), and the odd-power subspace has dimension \(b=\lfloor d/2\rfloor\). The operator \(E+M_{h(t^2)}\) acts on these two spaces, respectively, as multiplication by \(h(s)\) modulo \(s^h\) and multiplication by \(1+h(s)\) modulo \(s^b\). Let \(c=w(0)\). If \(c\notin\{0,a\}\), both multiplication operators are invertible, so \(D\) has rank \(n\). There are \((q-1)(q-2)q^{d-1}q^d=(q-1)(q-2)q^{2d-1}\) such derivations, proving the nonsingular term.

If \(c=0\), only the even block can have a kernel; if \(c=a\), only the odd block can have a kernel. In either case the relevant multiplication polynomial has constant coefficient zero and otherwise uniformly distributed coefficients, as proved above. For a length-\(\ell\) truncated polynomial module, its kernel dimension \(j\) is the truncated valuation: for \(1\le j<\ell\), the first nonzero coefficient is at position \(j\), and \(j=\ell\) means all coefficients through degree \(\ell-1\) vanish. Fixing \(a\) and \(c\), there are thus precisely
\[
(q-1)q^{d-1-j}\quad(1\le j<\ell),
\qquad q^{d-\ell}\quad(j=\ell)
\]
choices of \(w\) with kernel dimension \(j\). These are the \(W_\ell(j)\). Every choice of \(v\in R\) is allowed, contributing a factor \(q^d\); there are \(q-1\) choices of \(a\ne0\). Since \(D\) has rank \(n-j\), this gives precisely the last two sums, completing the proof.

**5. Normalization and nonsingularity.** The mutually exclusive cases \(a=0\), \(a\ne0,c\notin\{0,a\}\), \(a\ne0,c=0\), \(a\ne0,c=a\) partition all \(q^{2d+1}\) derivations. Their counts total that power because \(\sum_{j=1}^{\ell}W_\ell(j)=q^{d-1}\). A derivation is invertible exactly in the nonresonant case \(a\ne0,c\notin\{0,a\}\), yielding the asserted fraction. When \(q=2\), no such \(c\) exists.

## Verification

Execute `python3 verify.py` with a standard Python 3 interpreter. The self-contained program builds the Lie bracket and the derivation matrix independently, computes ranks by finite-field Gaussian elimination, and compares complete histograms against the closed polynomial. It exhausts all parameter triples for \(q=2\), \(4\le n\le8\), and for \(q=4\), \(n=4,5\); it also performs random tests for \(q=4,8\), checks all \(2^{16}\) linear maps in the four-dimensional binary case for the derivation identity, and checks the gauge-conjugation identity on 960 randomly chosen examples. Successful execution prints `VERIFY_OK_FILIFORM_DERIVATION_RANKS`. For instance, the full histogram for \((q,n)=(2,4)\), in increasing-rank order, is \((1,9,30,88,0)\). These finite checks support but do not replace the proof for all dimensions and fields.

## Relationship to prior work

The model filiform Lie algebra is classical. Bahturin–Goze–Remm (2013) describe its structure while classifying gradings, primarily in characteristic different from two. Tsartsaflis (2017) studies cohomology and Betti numbers for characteristic-two model filiform Lie algebras, including the same bracket model. Sheng–Liu–Liu (2024), especially the derivation normal form in their Section 3, treat model filiform Lie superalgebras in characteristic zero. These are antecedents for the algebra and derivation formalism, not assertions of the complete finite-field, characteristic-two rank distribution proved here. The standard bibliography also includes the 1996 monograph of Goze–Khakimdjanov; the relevant full monograph was not available for complete checking. The proof's substantive ingredient beyond the classical normal form is the characteristic-two odd/even gauge reduction and its exact rank-counting consequence. Literature priority is not certified by unsuccessful searches.

## Limitations

The theorem does not claim a classification for odd characteristic, smaller dimensions, arbitrary filiform deformations, automorphism orbit counts, or the geometry of derivation-rank loci as schemes. No independent mathematical audit has been performed. It is possible that equivalent enumerative results exist under the language of truncated-polynomial differential operators, modular filiform derivations, or finite linear algebra; the inaccessible 1996 monograph is a particular residual source of uncertainty.

## References

1. Y. Bahturin, M. Goze, E. Remm, *Group gradings on filiform Lie algebras*, arXiv:1308.2396v1, public 11 August 2013. https://arxiv.org/html/1308.2396v1
2. D. Tsartsaflis, *On the Betti Numbers of Filiform Lie Algebras over Fields of Characteristic Two*, Revista de la Unión Matemática Argentina 58 (2017), 95–106, online 9 February 2017. https://inmabb.criba.edu.ar/revuma/pdf/v58n1/v58n1a07.pdf
3. Y. Sheng, W. Liu, Y. Liu, *Local Automorphisms and Local Superderivations of Model Filiform Lie Superalgebras*, Journal of Mathematics (2024), article 6650997, doi:10.1155/2024/6650997. https://onlinelibrary.wiley.com/doi/10.1155/2024/6650997
4. M. Goze, Y. Khakimdjanov, *Nilpotent Lie Algebras*, Kluwer Academic Publishers, 1996. The complete text was not inspected.
