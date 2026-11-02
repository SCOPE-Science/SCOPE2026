# Effective eventual symmetry for parity-lifted denumerants and the exact \(\langle6,7,8\rangle\) spectrum

## Finding

**Theorem (effective tail rigidity and a sharp progression spectrum).** Let \(a,b,c\ge2\) be pairwise coprime integers, with \(c\ge3\) odd, and put \(A=(2a,2b,c)\). For each integer \(n\ge0\), let \(d_A(n)\) be the number of triples of nonnegative integers \((x,y,z)\) satisfying \(2ax+2by+cz=n\). For \(p\ge0\), define the threshold set \(S_p(A)=\{n\ge0:d_A(n)>p\}\), its smallest element \(\ell_p\), its greatest missing nonnegative integer \(g_p\), and its number of missing nonnegative integers \(n_p\).

Let \(H(t)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3:ax+by+cz=t\}\), and define the **finite, explicit** integers
\[
L=abc,\qquad \delta=\min_{0\le r<L}\bigl(H(r+1)-H(r)\bigr),\qquad
J=\max(0,1-\delta),\qquad U=JL,
\]
\[
P=\max\bigl(\{0\}\cup\{H(t):0\le t<U\}\bigr).
\]
Every quantity in the definition of \(P\) is obtained from a finite coin-count calculation. For every integer \(p\ge P\), set \(u_p=\min\{t\ge0:H(t)>p\}\). Then
\[
\boxed{S_p(2a,2b,c)=2u_p+\langle2,c\rangle,}
\]
where \(\langle2,c\rangle=\{2x+cy:x,y\in\mathbb Z_{\ge0}\}\). In particular,
\[
\boxed{\ell_p=2u_p,\qquad g_p=2u_p+c-2,\qquad n_p=2u_p+\frac{c-1}{2}.}
\]
Thus every sufficiently high representation threshold is \(p\)-symmetric in the sense of \(2n_p=\ell_p+g_p+1\), and this conclusion has a finite, computable onset bound for **every** specified triple under the hypotheses.

For the natural three-term arithmetic progression \(A=(6,7,8)\), the stronger **complete, sharp classification** holds:
\[
\boxed{S_p(6,7,8)\text{ is }p\text{-symmetric}\quad\Longleftrightarrow\quad p\ne1\qquad(p\in\mathbb Z_{\ge0}).}
\]
This includes arbitrarily high \(p\), the previously undetermined range beyond the low-threshold formulas; at \(p=7\) the intermediate threshold set is not a ray, yet it remains \(p\)-symmetric.

## Assumptions and scope

The triple is *ordered for counting*: a representation is a nonnegative integer coefficient triple, not a partition up to order. The three integers \(a,b,c\) are pairwise coprime and at least two; \(c\) is odd and at least three; \(p\) is a nonnegative integer. The triple need not be a minimal generating set, and the theorem does not assume \(c\in\langle a,b\rangle\). The set \(2u_p+\langle2,c\rangle\) is a **translated ideal**, not asserted to be an additive monoid containing zero when \(u_p>0\).

The specific progression \((6,7,8)\) corresponds to \((a,b,c)=(3,4,7)\). The criterion for \(p\)-symmetry is the equivalent genus formula of Komatsu–Ying; it also agrees with the gap-reflection definition. When \(p=0\) the least element is zero, as usual.

## Proof

**1. Parity splitting.** For every \(t\ge0\), an even target \(2t\) forces the coefficient of odd \(c\) to be even, while an odd target \(2t+c\) forces that coefficient to be odd. Substituting \(z=2w\) and \(z=2w+1\) proves the two exact bijections
\[
 d_A(2t)=H(t)=d_A(2t+c).
\]
There are no odd representations below \(c\). Thus, for **every** \(p\ge0\) (without an eventuality condition), with \(T_p=\{t\ge0:H(t)>p\}\),
\[
S_p(A)=2T_p\ \cup\ (c+2T_p).
\]
The two components are disjoint by parity.

**2. Exact quadratic-periodic denumerant law.** The generating series for \(H\) is
\[
F(z)=\frac1{(1-z^a)(1-z^b)(1-z^c)}.
\]
Pairwise coprimality ensures every pole at a nontrivial root of unity is simple; all such poles have orders dividing \(L=abc\). At \(z=1\), the principal part is
\[
\frac{1}{L(1-z)^3}+\frac{a+b+c-3}{2L(1-z)^2}+\frac{C}{1-z}
\]
for some rational constant \(C\). Partial fractions therefore give
\[
H(t)=\frac{t^2}{2L}+\frac{(a+b+c)t}{2L}+Q(t),
\]
with \(Q\) periodic with period dividing \(L\). Subtracting at indices \(t+L\) and \(t\) gives the **exact integer identity**
\[
\boxed{H(t+L)-H(t)=t+\frac{L+a+b+c}{2}\qquad(t\ge0).}
\]
The half-integer-looking constant is integral, because either all three generators are odd or exactly one is even. Taking consecutive differences, with \(\Delta(t)=H(t+1)-H(t)\), yields
\[
\Delta(t+L)=\Delta(t)+1.
\]
Consequently \(\Delta(r+kL)\ge\delta+k\ge1\) for all \(0\le r<L\) and \(k\ge J\). This proves \(H\) is strictly increasing on the entire tail \(t\ge U\), rather than merely on a subsequence.

**3. Effective onset and genus.** If \(p\ge P\), then \(H(t)\le p\) for every \(0\le t<U\); on the tail \(H\) is strictly increasing and tends to infinity. Therefore \(T_p=\{u_p,u_p+1,\ldots\}\), with \(u_p\ge U\). The parity decomposition becomes
\[
S_p(A)=\{2u_p+2j:j\ge0\}\cup\{2u_p+c+2j:j\ge0\}=2u_p+\langle2,c\rangle.
\]
Because \(c\) is odd, the positive gaps of \(\langle2,c\rangle\) are the \((c-1)/2\) odd integers below \(c\), with largest gap \(c-2\). Translating by \(2u_p\) adds exactly \(2u_p\) initial gaps. Hence the displayed formulas for \(\ell_p,g_p,n_p\) follow and give \(2n_p=\ell_p+g_p+1\). This also verifies gap-reflection symmetry directly.

**4. Sharp classification for \((6,7,8)\).** Here \(H\) counts representations by \((3,4,7)\) and \(L=84\). To give an explicitly checkable finite certificate, for \(v\ge0\) define
\[
 r_v\in\{0,1,2,3\},\quad r_v\equiv3v\pmod4,\qquad
 E(v)=\max\!\left(0,1+\left\lfloor\frac{\lfloor v/3\rfloor-r_v}{4}\right\rfloor\right).
\]
The equation \(3x+4y=v\) has \(x\equiv3v\pmod4\) and \(0\le x\le\lfloor v/3\rfloor\), so \(E(v)\) counts its solutions **exactly**. Thus
\[
H(t)=\sum_{j=0}^{\lfloor t/7\rfloor} E(t-7j).
\]
Substitution supplies the following exhaustive \(84\)-residue table of consecutive differences \(\Delta(t)=H(t+1)-H(t)\). Entries are listed in increasing index order within each range.

| Index range | Exact differences |
|:--|:--|
| 0–11 | -1, 0, 1, 0, -1, 1, 1, -1, 0, 1, 0, 0 |
| 12–23 | 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1 |
| 24–35 | 0, 0, 1, 1, -1, 1, 1, 0, 0, 1, 1, 0 |
| 36–47 | 0, 1, 1, 0, 0, 2, 0, 0, 1, 1, 0, 1 |
| 48–59 | 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1 |
| 60–71 | 0, 1, 2, 0, 0, 2, 1, 0, 1, 2, 0, 1 |
| 72–83 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2 |

The only negative entries are \(\Delta(0)=\Delta(4)=\Delta(7)=\Delta(28)=-1\). Since \(\Delta(t+84)=\Delta(t)+1\), **all** later differences are nonnegative, and in fact \(H\) is nondecreasing from index \(29\) onward. Explicit evaluation for \(0\le t\le31\) gives the entire non-ray portion and these threshold sets:

| \(p\) | \(T_p=\{t:H(t)>p\}\) |
|:--|:--|
| \(0\) | \(\mathbb Z_{\ge0}\setminus\{1,2,5\}\) |
| \(1\) | \(\{7\}\cup\{t\ge10\}\) |
| \(2\) | \(\{t\ge14\}\) |
| \(3\) | \(\{t\ge18\}\) |
| \(4\) | \(\{t\ge21\}\) |
| \(5\) | \(\{t\ge24\}\) |
| \(6\) | \(\{t\ge27\}\) |
| \(7\) | \(\{28\}\cup\{t\ge30\}\) |
| \(p\ge8\) | A terminal ray (its start depends on \(p\)) |

Indeed \(\max_{0\le t\le30}H(t)=8\) and \(H(31)=9\), so monotonicity from \(29\) proves the last row for **every** \(p\ge8\), not merely checked instances. All rows except \(p\in\{0,1,7\}\) are rays and hence symmetric by Step 3's elementary parity-and-gap argument (which applies to any ray without its bound).

For \(p=0\), direct parity splitting gives the ordinary symmetric numerical semigroup \(\langle6,7,8\rangle\) with gaps \(\{1,2,3,4,5,9,10,11,17\}\), so \((\ell_0,g_0,n_0)=(0,17,9)\) and \(2n_0=\ell_0+g_0+1\). For \(p=1\), the three parameters are \((\ell_1,g_1,n_1)=(14,25,21)\), and \(42\ne40\), so \(p\)-symmetry fails. For \(p=7\), they are \((\ell_7,g_7,n_7)=(56,65,61)\), and \(122=122\), so symmetry holds despite the single hole in \(T_7\). This exhausts every threshold and completes the proof.

## Verification

`verify.py` is a Python 3 standard-library verifier. It reconstructs the generating-function coefficients by independent coin-change dynamic programming, independently counts two- and three-coin solutions for small instances, checks the exact period-shift identity, the parity bijection, effective tail thresholds and the entire sharp spectrum. It tests the direct genus criterion for \(p=0,1,\ldots,100\); its primary certificate is the **complete 84-entry difference table plus the algebraic period-shift identity**, not an inference from the 101 tested thresholds.

To reproduce: `python3 verify.py`. The recorded output is `VERIFY_OK finite_identities=4317 spectrum_levels=101 exceptional_level=1`.

## Relationship to prior work

Komatsu and Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions* (first public 27 June 2022), give formulas for \(0\le p\le\lfloor a/2\rfloor\) for \((a,a+d,a+2d)\). Their related *\(p\)-numerical semigroups with \(p\)-symmetric properties* (first public 18 July 2022) defines symmetry and proves selected low-threshold symmetry, including an even-first-generator case. These results do not determine the **entire** \((6,7,8)\) symmetry spectrum or an effective all-high-\(p\) translated-ideal law for arbitrary parity-coupled triples.

Komatsu, *\(p\)-numerical semigroups with \(p\)-symmetric properties, II* (first public 4 September 2024), proves a Watanabe-type equivalence for \((\alpha,\beta b_1,\ldots,\beta b_k)\) under the additional condition \(\alpha\in\langle b_1,\ldots,b_k\rangle\). That result bears on the **subclass** \(c\in\langle a,b\rangle\), but does not alone supply the explicit threshold-ray identity, effective onset, or the cases \(c\notin\langle a,b\rangle\), for example \((a,b,c)=(3,4,5)\). The theorem here counts representations using all three generators, including any redundant generator, exactly as the definition requires.

## Limitations

No exact smallest possible onset \(P\) is claimed; the finite bound is deliberately conservative (for the progression \((6,7,8)\), the stronger bound \(p\ge8\) is established separately). The general theorem requires pairwise coprime half-generators and an odd third generator. It does not assert an analogous result for arbitrary three-generator systems of mixed parity. The period-shift identity rests on elementary quasi-polynomial partial fractions; this proof does not claim that the technique alone is new. A possibly unindexed equivalent specialization in the numerical-semigroup literature remains a priority risk; no independent scientific audit has been conducted.

## References

1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (v1, 27 June 2022), https://arxiv.org/abs/2206.13052.
2. T. Komatsu and H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962 (v1, 18 July 2022), https://arxiv.org/abs/2207.08962.
3. T. Komatsu, *\(p\)-numerical semigroups with \(p\)-symmetric properties, II*, arXiv:2409.02394 (v1, 4 September 2024), https://arxiv.org/abs/2409.02394.
