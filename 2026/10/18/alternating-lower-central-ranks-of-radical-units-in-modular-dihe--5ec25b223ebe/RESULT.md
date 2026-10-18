# Alternating lower-central ranks of radical units in modular dihedral group algebras

## Finding

Let \(p\ge3\) be prime, \(q=p^f\) with \(f\ge1\), and \(D_{2p}=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle\). Put \(A=\mathbb F_q[D_{2p}]\), \(J=\operatorname{Jac}(A)\), \(U=1+J\), and \(\ell=(p-1)/2\). Define the lower central series by \(\gamma_1(U)=U\), \(\gamma_{i+1}(U)=[\gamma_i(U),U]\).

The entire lower central series is determined by the following elementary-abelian quotients, written as additive \(\mathbb F_q\)-groups:
\[
\gamma_1(U)/\gamma_2(U)\cong (\mathbb F_q,+)^{\ell+2},\qquad
\gamma_{2j}(U)/\gamma_{2j+1}(U)\cong(\mathbb F_q,+)\ (1\le j\le\ell),
\]
\[
\gamma_{2j+1}(U)/\gamma_{2j+2}(U)\cong(\mathbb F_q,+)^2\ (1\le j<\ell).
\]
In particular \(\gamma_{p-1}(U)\ne1=\gamma_p(U)\), so the nilpotency class is **exactly** \(p-1\), attaining the radical-filtration upper bound. The orders of the terms are
\[
|\gamma_{2j}(U)|=q^{3(\ell-j)+1},\qquad
|\gamma_{2j+1}(U)|=q^{3(\ell-j)}\quad(1\le j\le\ell),
\]
with \(|U|=q^{4\ell}=q^{2(p-1)}\), \(|[U,U]|=q^{3\ell-2}\), and the minimal number of abstract generators equal to \(f(\ell+2)\).

## Assumptions and scope

All groups are finite and all commutators use the convention \([a,b]=a^{-1}b^{-1}ab\). The coefficient field has characteristic \(p\), with the same odd prime appearing in the order \(2p\) of the dihedral group; no algebraic-closedness assumption is used. A statement that a quotient is an additive \(\mathbb F_q\)-group refers to its induced elementary-abelian group structure, not a claimed canonical \(\mathbb F_q\)-linear structure on all of \(U\). The result concerns the distinguished Sylow \(p\)-subgroup \(1+J\), not the lower central series of the full unit group \(A^\times\).

## Proof

**1. A reflection-odd uniformizer.** In \(B=\mathbb F_q[\langle r\rangle]\), write \(t=r-1\). As \(r^p-1=t^p\) in characteristic \(p\), \(B\cong k[t]/(t^p)\), where \(k=\mathbb F_q\). The element \(r+r^{-1}\) has constant term \(2\) and is invertible. Define
\[
u=(r-r^{-1})(r+r^{-1})^{-1}.
\]
It satisfies \(u=t+O(t^2)\) and hence generates the maximal ideal of \(B\); conjugation by \(s\) sends \(u\) to \(-u\). Consequently
\[
A\cong k\langle u,s\rangle/(u^p,\ s^2-1,\ su+us),
\quad J=uA,
\quad A/J\cong k[C_2]\cong k\times k.
\]
Here \(J^p=0\), \(\dim_kJ=2(p-1)=4\ell\), and \(J\) is exactly the Jacobson radical. The unit group quotient \(A^\times/(1+J)\cong(k^\times)^2\) has order prime to \(p\), so \(U=1+J\) is its unique Sylow \(p\)-subgroup. Moreover \((1+x)^p=1+x^p=1\) for every \(x\in J\), giving exponent \(p\).

**2. A four-family Lie basis.** Let \(e_+=(1+s)/2\), \(e_-=(1-s)/2\), and \(v=u^2\). For \(1\le i\le\ell\), set
\[
C_i=v^i(e_++e_-),\qquad H_i=v^i(e_+-e_-),
\]
and, for \(0\le j<\ell\), set
\[
E_j=v^j e_+ue_-,\qquad F_j=v^j e_-ue_+.
\]
These \(4\ell\) elements form a \(k\)-basis of \(J\). In the Lie algebra \(L=(J,[x,y]=xy-yx)\), every \(C_i\) is central, and the only nonzero basic brackets, with out-of-range indices interpreted as zero, are
\[
[E_i,F_j]=H_{i+j+1},\qquad
[H_i,E_j]=2E_{i+j},\qquad
[H_i,F_j]=-2F_{i+j}.
\]
Indeed the off-diagonal matrix units multiply as \(E_iF_j=v^{i+j+1}e_+\) and \(F_jE_i=v^{i+j+1}e_-\). The coefficient \(2\) is nonzero precisely because \(p\) is odd.

**3. The Lie lower central series.** Write \(L_1=L\) and \(L_{a+1}=[L_a,L]\). From the displayed bracket table, for every \(1\le j\le\ell\),
\[
L_{2j}=\operatorname{span}_k\{H_i:j\le i\le\ell\}
\oplus\operatorname{span}_k\{E_i,F_i:j\le i<\ell\},
\]
\[
L_{2j+1}=\operatorname{span}_k\{H_i:j+1\le i\le\ell\}
\oplus\operatorname{span}_k\{E_i,F_i:j\le i<\ell\}.
\]
To justify equality, not merely inclusion, observe that \([E_0,F_{j-1}]=H_j\) and \([H_j,E_0]=2E_j\), \([H_j,F_0]=-2F_j\) wherever the indices exist. These identities and their shifted versions generate each boundary basis vector inductively, while the bracket table forbids lower indices. In particular \(L_{2\ell}=kH_\ell\ne0\) and \(L_{2\ell+1}=0\). Counting basis vectors yields
\[
\dim_kL_{2j}=3(\ell-j)+1,\qquad
\dim_kL_{2j+1}=3(\ell-j).
\]

**4. Passage from the Lie algebra to the group.** Because \(J^p=0\), the finite polynomials
\[
\exp(x)=\sum_{a=0}^{p-1}\frac{x^a}{a!},\qquad
\log(1+x)=\sum_{a=1}^{p-1}\frac{(-1)^{a+1}x^a}{a}
\]
are mutually inverse bijections from \(J\) to \(1+J\). The truncated Baker--Campbell--Hausdorff identities of weights below \(p\) are valid in characteristic \(p\): their denominators are prime to \(p\). Equivalently, the Lazard correspondence in class less than \(p\) sends the lower central series of \(L\) to that of the group \(U\). Thus \(\gamma_i(U)=\exp(L_i)\) for all \(i\). This step is a finite nilpotent identity, not an inference from finite-field experiments.

The dimension formulas now give the claimed orders and additive quotient types. Finally, the exponent-\(p\) property makes the Frattini subgroup equal to \([U,U]\), so the abstract generator rank is \(f\dim_k(L/L_2)=f(\ell+2)\).

## Verification

Run `python3 verify.py` using only the Python standard library. It independently forms the radical bracket algebra from block multiplication, computes every Lie lower central subspace by modular Gaussian elimination for \(p=3,5,7,11,13,17\), and compares the resulting dimensions with the closed formulas. It also constructs the original truncated crossed-product multiplication: for \(p=3\), all \(81^2=6561\) ordered pairs of radical units are checked, the commutator set has size \(3\), and all these commutators are central. Further finite tests exercise truncated exponential, logarithm, and commutator leading terms for \(p=3,5,7\). The expected terminal line is `VERIFY_OK_LOWER_CENTRAL`. These checks corroborate but do not prove the arbitrary-prime and arbitrary-extension-degree statements.

## Relationship to prior work

Gildea's 2009 article computes the **center** of the maximal \(p\)-subgroup of \(\mathbb F_{p^f}[D_{2p}]^\times\), finding its elementary-abelian order. Kaur and Khan's 2013 work gives a decomposition of that subgroup, its order and exponent, and the bound that its nilpotency class is at most \(p-1\). The present calculation gives a different invariant: each lower-central quotient, together with the sharpness of that bound. Their conclusions about the center, exponent and size are used only as literature context; the proof here independently reconstructs the ring presentation and all brackets. Earlier papers on small primes and the original modular dihedral algebras are relevant background, but are not claimed to be superseded by this result.

## Limitations

No claim is made about the corresponding subgroup for \(D_{2p^a}\) with \(a>1\), about characteristic \(2\), or about the full unit group. The Lie-series and group-series identification uses the odd-prime, class-less-than-\(p\) hypothesis. The inspected sources do not establish absolute priority: an equivalent lower-central calculation in older group-presentation literature may remain unlocated. The finite computations are sample checks, not infinite certificates. Independent external validation has not been performed.

## References

1. J. Gildea, *The centre of the maximal \(p\)-subgroup of \(\mathcal U(\mathbb F_{p^k}D_{2p})\)*, Glasgow Mathematical Journal **51** (2009), 651--657, DOI: `10.1017/S0017089509990061`, first online 2009-09-01.
2. K. Kaur and M. Khan, *Units in \(FD_{2p}\)*, arXiv:`1305.1260`, first public version 2013-05-06.
3. A. V. Jeyakumar, *Group Algebras of Dihedral and Dicyclic Groups Over Modular Fields*, Journal of the London Mathematical Society **s2-2** (1970), 297--304, DOI: `10.1112/jlms/s2-2.2.297` (context; detailed theorem coverage not independently resolved).
