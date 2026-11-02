# Adjoint-centralizer spectra and a characteristic-two parity isomorphism for truncated polynomial derivations

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\), and let \(N\ge2\). The Lie algebra \(L_N=\operatorname{Der}_k(k[t]/(t^N))\) has a completely explicit centralizer and adjoint-nullity distribution. Put \(\ell=0\) if \(p\mid N\), and \(\ell=1\) otherwise, and \(d=N-\ell\). For \(\ell\le v<N\), set
\[
 c_N(v)=\#\{j:\ell\le j<N,\ j+v-1\ge N\ \text{or}\ j\equiv v\pmod p\}.
\]
The number of derivations whose adjoint action has nullity \(c\) is the coefficient of \(z^c\) in
\[
 P_{N,q}(z)=z^d+\sum_{v=\ell}^{N-1}(q-1)q^{N-v-1}z^{c_N(v)}.
\]
In particular, the number of ordered commuting derivation pairs is \(P_{N,q}(q)\). If \(N=kp\), with \(k\ge1\), this count simplifies to
\[
 q^N+(q^{N+k}-q^N)S_p(q),\quad
 S_p(q)=\begin{cases}1+q^{-1},&p=2,\\1+\frac{p-1}{2}(q^{-1}+q^{-2}),&p>2.\end{cases}
\]
The displayed expression is an integer; the fractions describe exact powers of \(q\).

Moreover, in characteristic two, for every field \(k\) and every \(r\ge1\), there is an explicit isomorphism of ordinary Lie algebras
\[
 L_{2r}\ \cong\ L_{2r+1}\ \cong\ k[z]/(z^r)\rtimes k[z]/(z^r),
\]
where the second, abelian summand acts on the first by multiplication. Over \(\mathbb F_q\) with \(q\) even, their common complete adjoint-nullity polynomial is
\[
 P_{2r,q}(z)=P_{2r+1,q}(z)=z^{2r}+\sum_{s=0}^{r-1}(q^2-1)q^{2(r-s-1)}z^{r+s}.
\]
Their identical number of commuting ordered pairs is
\[
 (q+1)q^{3r-1}-q^{2r-1}.
\]
The parity isomorphism concerns Lie algebras of derivations; it does not assert the underlying truncated associative algebras are isomorphic.

## Assumptions and scope
The ground field is any finite field for the counting results, with no restriction on its extension degree. For the characteristic-two Lie-algebra isomorphism the ground field may be arbitrary. Every derivation is \(D_f=f(t)\,d/dt\). The relation \(t^N=0\) imposes \(Nt^{N-1}f(t)=0\); hence \(f\) is divisible by \(t\) exactly when \(p\nmid N\). Thus \(f\) ranges over the \(d\)-dimensional span of \(t^j\), \(\ell\le j<N\). The bracket is \([D_f,D_g]=D_{fg'-gf'}\), and centralizers are defined for the *ordinary* Lie bracket, not for the restricted Lie structure. Nullity means \(\dim_k\ker(\operatorname{ad}_{D_f})\). Valuations are least nonzero coefficient degrees, with \(v(0)=N\). The output counts derivations as labeled elements, and ordered pairs, not conjugacy classes.

## Proof
**1. Complete centralizer subspaces.** For nonzero \(f=t^v u\) with \(u(0)\ne0\), write \(g=uh\). Multiplication by the unit \(u\) bijects the admissible coefficient space \(t^\ell k[t]/(t^N)\) with itself. Direct differentiation, including when \(v=0\), gives
\[
 fg'-gf'=u^2t^v h'-v u^2t^{v-1}h.
\]
For \(h=\sum_{j=\ell}^{N-1}h_jt^j\), its coefficient attached to each index \(j\) is \((j-v)h_jt^{j+v-1}\). The monomial exponents are distinct, so the bracket is zero modulo \(t^N\) if and only if every coefficient with \(j+v-1<N\) and \(j\not\equiv v\pmod p\) vanishes. For \(v=j=0\), the formal negative exponent has zero coefficient and is omitted. Consequently
\[
 C_{L_N}(D_f)=\left\{D_{u h}:h\in\operatorname{span}_k\{t^j:\ell\le j<N,\ j+v-1\ge N\text{ or }j\equiv v\pmod p\}\right\},
\]
which proves the centralizer dimension formula. For \(f=0\), all of \(L_N\) centralizes it.

**2. Multiplicities and finite-field polynomial.** Every admissible valuation \(v\) has \((q-1)q^{N-v-1}\) coefficients \(f\), since its first nonzero coefficient has \(q-1\) choices and the higher coefficients are free. Add the unique zero element to obtain \(P_{N,q}\), and sum \(q^{\dim C_{L_N}(D_f)}\) over all \(f\) to obtain the commuting-pair count. This uses no assumption that the ordinary Lie algebra is restricted.

**3. Closed count when \(p\mid N\).** Write \(N=kp\), \(v=ap+b\), with \(0\le a<k\), \(0\le b<p\). Counting the admissible \(j\)'s directly in part 1 gives
\[
 c_N(ap+b)=k+(p-1)a+b-\left\lceil\frac{2b}{p}\right\rceil.
\]
Therefore, on separating the zero derivation,
\[
 P_{N,q}(q)-q^N=(q-1)q^{N+k-1}
 \sum_{a=0}^{k-1}q^{-a}\sum_{b=0}^{p-1}q^{-\lceil2b/p\rceil}
 = (q^{N+k}-q^N)S_p(q).
\]
For \(p=2\), the final finite sum is \(1+q^{-1}\). For odd \(p\), the \(p-1\) nonzero residues split into two equally numerous ranges contributing \(q^{-1}\) and \(q^{-2}\), proving the closed form.

**4. Characteristic-two normal form.** Fix characteristic two and \(r\ge1\). For \(L_{2r}\), take \(A_j=D_{t^{2j}}\) and \(B_j=D_{t^{2j+1}}\), \(0\le j<r\). For \(L_{2r+1}\), take \(A'_j=D_{t^{2j+2}}\) and \(B'_j=D_{t^{2j+1}}\), again \(0\le j<r\). These are bases of the respective derivation Lie algebras: the even-length algebra admits a constant coefficient, while the odd-length one does not. Since the commutator of basis derivations satisfies
\[
 [D_{t^i},D_{t^j}]=(j-i)D_{t^{i+j-1}},
\]
and arithmetic is in characteristic two, in either basis the only nonzero brackets are
\[
 [B_i,A_j]=A_{i+j}\quad(i+j<r),\qquad [B'_i,A'_j]=A'_{i+j}\quad(i+j<r),
\]
with all brackets indexed \(i+j\ge r\) and all \([A,A]\), \([B,B]\) zero. Identify the \(A_j\) with \((z^j,0)\) and \(B_j\) with \((0,z^j)\) in \(S_r\oplus S_r\), \(S_r=k[z]/(z^r)\), using bracket \([(a,b),(a',b')]=(ba'-b'a,0)\). This supplies an isomorphism for every \(r\), not merely a dimension count.

**5. Entire spectrum in characteristic two.** For \((a,b)\in S_r^2\), the image of its adjoint action on \(S_r^2\) is the ideal \(aS_r+bS_r\). If \(s=\min\{v_z(a),v_z(b)\}\), taking \(v_z(0)=r\), that ideal is \(z^sS_r\), of dimension \(r-s\). Thus the adjoint nullity is \(r+s\). For \(0\le s<r\), exactly \((q^2-1)q^{2(r-s-1)}\) ordered pairs \((a,b)\) have minimum valuation \(s\); at \(s=r\) there is only \((0,0)\). These give the stated full spectrum and show the parity equality. Summing their centralizer cardinalities yields
\[
 q^{2r}+\sum_{s=0}^{r-1}(q^2-1)q^{2(r-s-1)}q^{r+s}
 =(q+1)q^{3r-1}-q^{2r-1}.
\]

## Verification
The accompanying self-contained `check_census.py` constructs the coefficient matrix of \(\operatorname{ad}_{D_f}\) directly, uses finite-field Gaussian elimination, enumerates every admissible \(f\) in 24 finite-field/truncation configurations, and compares the resulting nullity histogram with the proved formulas. It separately checks the closed count for every tested \(N\) divisible by \(p\). The verified execution ended with `TRUNCATED_DERIVATION_ADJOINT_CENSUS_OK 24 10678`. Configurations include prime fields and quadratic extensions in characteristics two and three. These finite tests are not a proof for unbounded \(N\); steps 1–5 are the proof.

## Relationship to prior work
Yao and Chang, *Nilpotent commuting varieties of the Witt algebra* (arXiv:1301.5667v1, publicly posted 2013-01-23), give explicit centralizer information for the classical \(p\)-dimensional Witt algebra over algebraically closed fields in characteristic \(p>3\), including their Lemma 2.3. That literature **already covers part of the \(N=p\) centralizer structure** (and may entail part of a special counting case after finite-field specialization). No priority is claimed for those components. Premet, *Regular derivations of truncated polynomial rings* (arXiv:1405.2426v1, 2014-05-10), studies regular derivations and centralizers of restricted Jacobson–Witt algebras associated with variables truncated at characteristic \(p\), in characteristic greater than two. Neither inspected primary study states or implies the all-length full finite-field nullity distribution together with the explicit characteristic-two consecutive-length affine isomorphism. The stronger normal form and parity collapse involve characteristic two, excluded by the characteristic assumptions of these works. Relevant other work on filiform Lie algebra adjoint spectra and finite Kronecker path-algebra commutativity does not entail this derivation-specific statement.

## Limitations
The full distribution is for derivations of **one-variable** truncated polynomial algebras. The closed simplified commuting-pair formula is stated for truncation lengths divisible by the characteristic, while the full polynomial covers all lengths. The parity isomorphism requires characteristic two. Results do not classify isomorphism types of underlying associative algebras, conjugacy classes, general vector fields in several variables, or the full scheme of commuting derivations. Earlier or unindexed modular Lie-algebra papers might contain an equivalent specialization; absence from the searched sources does not prove publication priority. Independent mathematical review has not been performed.

## References
1. Yu-Feng Yao and Hao Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1 (first posted 2013-01-23), https://arxiv.org/abs/1301.5667 . Centralizer Lemma 2.3 concerns the classical restricted Witt algebra.
2. Alexander Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v1 (first posted 2014-05-10), https://arxiv.org/abs/1405.2426 . Regular-derivation strata in modular Cartan-type Lie algebras.
3. *Adjoint-rank spectra of two maximal-class filiform Lie algebras*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-adjoint-rank-spectra-of-two-maximal-class-filiform-lie-algebras--48cdbeaf7d86 . Different Lie algebra families and not an implication of the present claim.
