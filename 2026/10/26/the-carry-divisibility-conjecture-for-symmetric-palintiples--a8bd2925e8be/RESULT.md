# The carry divisibility conjecture for symmetric palintiples

## Finding

**Theorem.** Let \(n,b,k\) be integers with \(1<n<b\) and \(k\ge1\). Let the base-\(b\) number with digits \(d_k,\ldots,d_0\), where \(0\le d_j<b\), \(d_0d_k\ne0\), satisfy
\[
(d_kd_{k-1}\cdots d_0)_b=n(d_0d_1\cdots d_k)_b.
\]
Let \(c_0=0,c_1,\ldots,c_k,c_{k+1}=0\) be the carries of multiplication by \(n\) on the reversed digits, with \(0\le c_j\le n-1\). If the carries are symmetric, meaning \(c_j=c_{k-j}\) for \(0\le j\le k\), then
\[
(n-1)\mid c_j \quad(0\le j\le k),\qquad c_j\in\{0,n-1\},\qquad n+1\mid b.
\]
In conjunction with Holt's published converse, a palintiple has symmetric carries **if and only if** \(n+1\mid b\); for all such \((n,b)\), at least one palintiple exists.

## Assumptions and scope

The base and multiplier are positive integers with \(1<n<b\), the representation is of finite length, and **both leading and trailing digits are nonzero**, ruling out leading zeros after reversal. Zero and one-digit trivialities and multiplier \(1\) are outside the statement. All claims are exact for every digit length, with no bound on \(n\), \(b\) or \(k\).

For an indexed digit string, the grade-school multiplication equations are
\[
bc_{j+1}-c_j=nd_{k-j}-d_j\quad(0\le j\le k),
\]
with \(c_0=c_{k+1}=0\). Eliminating the reversed digit gives the **integer identity**
\[
(n^2-1)d_j=nbc_{k-j+1}-nc_{k-j}+bc_{j+1}-c_j.
\tag{1}
\]
The standard carry bound \(0\le c_j\le n-1\) follows from the multiplication algorithm (or Holt 2014, Theorem 3).

## Proof

Suppose the carries are symmetric. Then \(c_k=c_0=0\). At \(j=0\), equation (1) gives
\[
(n^2-1)d_0=bc_1.
\tag{2}
\]
Since \(d_0>0\), one has \(c_1>0\). For \(1\le j\le k-1\), use symmetry \(c_{k-j+1}=c_{j-1}\) and \(c_{k-j}=c_j\) in (1), obtaining
\[
b(nc_{j-1}+c_{j+1})\equiv(n+1)c_j\pmod{n^2-1}.
\tag{3}
\]

Fix a prime \(\ell\mid n-1\), and let \(a=v_\ell(n-1)\ge1\), \(q=v_\ell(n+1)\ge0\), and \(t=v_\ell(b)\ge0\). Thus \(v_\ell(n^2-1)=a+q\). We prove \(\ell^a\mid c_j\) for every \(j\).

**Case \(t\le q\).** Equation (2) yields \(\ell^{a+q-t}\mid c_1\), in particular \(\ell^a\mid c_1\). Since \(c_0=0\), assume inductively that \(\ell^a\) divides both \(c_{j-1}\) and \(c_j\), for \(1\le j\le k-1\). The right side of (3) is divisible by \(\ell^{a+q}\); consequently, the left side is, and \(\ell^{a+q-t}\mid nc_{j-1}+c_{j+1}\). As \(a+q-t\ge a\), this implies \(\ell^a\mid c_{j+1}\). Induction proves the assertion.

**Case \(t>q\).** If some carry is not divisible by \(\ell^a\), let \(s<a\) be the least \(\ell\)-adic valuation of a nonzero carry. It is attained at some \(1\le j\le k-1\), because \(c_0=c_k=0\). Every carry is divisible by \(\ell^s\), so the left side of (3) is divisible by \(\ell^{t+s}\). Its right side has exact valuation \(q+s\), strictly smaller than \(t+s\) and than \(a+q\). Their difference therefore has valuation exactly \(q+s<a+q\), contradicting (3). So every carry is divisible by \(\ell^a\).

These two cases apply to every prime-power factor of \(n-1\); hence \((n-1)\mid c_j\). When \(n=2\) this conclusion is vacuous but still true. The universal bound \(0\le c_j\le n-1\) now gives \(c_j\in\{0,n-1\}\), and (2) with \(c_1>0\) forces \(c_1=n-1\). Canceling \(n-1\) in (2) yields \((n+1)d_0=b\), so \(n+1\mid b\).

For the reverse implication, Holt (2014), Theorem 6, proves that whenever \(n+1\mid b\), an \((n,b)\)-palintiple exists and *every* one has symmetric carries. Combining the two directions establishes the final equivalence. \(\square\)

## Verification

The accompanying standalone `verify.py` exhausts 409,838 symmetric bounded-carry tuples with \(2\le n\le12\), \(n<b\le40\), and \(3\le k+1\le8\). Exactly 384 tuples reconstruct valid reverse multiples; every one satisfies the carry conclusion and \(n+1\mid b\). The checks also reproduce the known examples \(87912=4\cdot21978\) and \(98901=9\cdot10989\). Run using `python3 verify.py` from a directory containing the embedded file. These are finite consistency checks: the universal conclusion is obtained from the proof above.

## Relationship to prior work

Holt (2014, Theorems 1, 3 and Corollary 2) supplies the carry identities and bound. Its Theorem 6 establishes the sufficient direction \(n+1\mid b\); Theorem 7 proves the converse only under \(\gcd(b,n-1)=1\), and the paper explicitly leaves the unrestricted converse open. Holt's subsequent *Some Thoughts on Determining Symmetric Palintiples* (2015 version of arXiv:1410.2356) states the carry divisibility assertion as **Conjecture 1** and derives the full symmetry/divisibility equivalence conditionally. The argument here supplies precisely that unproved arithmetic step via prime-local valuations.

Kendrick (arXiv:1410.0106, Theorem 3.1 and Remark 4) proves that the associated Young graph is the 1089 graph exactly when \(n+1\mid b\), but explicitly leaves the implication from the existence of a symmetric palintiple to that graph class conjectural. Holt (arXiv:2411.10859) develops enumeration and finite-state constructions for permutiples generally; no general symmetric-carry divisibility statement was located there. Holt (arXiv:2504.17158) studies *symmetric graph classes* arising from reflections of permutiple graphs, a different property from palindromic multiplication carries. None of the inspected statements provides the prime-local argument above.

## Limitations

This establishes the restricted symmetric-carry class, not a classification of all asymmetric or shifted-symmetric reverse multiples. The proof is elementary and unconditional under the stated digit conditions. Finite tests are illustrative, not exhaustive over infinite parameters. An equivalent theorem may exist in unlocated literature; no independent mathematical audit has been performed.

## References

1. B. V. Holt, *Some General Results and Open Questions on Palintiple Numbers*, **Integers** 14 (2014), Article A42, published 2014-08-27, https://www.maths.tcd.ie/EMIS/journals/INTEGERS/papers/o42/o42.pdf.
2. B. V. Holt, *Some Thoughts on Determining Symmetric Palintiples*, arXiv:1410.2356v2 (2015), https://arxiv.org/abs/1410.2356.
3. L. H. Kendrick, *Young Graphs: 1089 et Al.*, arXiv:1410.0106v3 (2015), https://arxiv.org/abs/1410.0106.
4. B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, arXiv:2411.10859v2 (2025), https://arxiv.org/abs/2411.10859.
5. B. V. Holt, *Utilizing Symmetry in Finding New Permutiples from Known Examples*, arXiv:2504.17158v3 (2025), https://arxiv.org/abs/2504.17158.
