# The sharp two-thirds partial-transversal law for nilpotent monogenic semigroups

## Finding
For every integer \(n\ge 2\), let \(N_n\) be the nilpotent monogenic semigroup on \(n\) elements defined below. The greatest possible number of entries of its multiplication table with pairwise distinct rows, columns, and products is exactly
\[
\tau(N_n)=\left\lfloor\frac{2n}{3}\right\rfloor.
\]
Both the upper bound and an explicit family of attaining partial transversals are valid for every \(n\). In particular, these semigroups have no full transversal once \(n\ge2\), but their optimal partial transversals occupy asymptotically two-thirds of the rows.

## Assumptions and scope
Let \(n\ge 2\) be an arbitrary integer. Write \(N_n=\{0,a,a^2,\ldots,a^{n-1}\}\), with \(a^n=0\), distinct displayed elements, and multiplication \(a^i a^j=a^{i+j}\) for \(i+j<n\), otherwise \(a^i a^j=0\). Here \(0\) is absorbing. A *partial transversal* is a set of table cells \((x,y)\) such that no two selected cells have the same row \(x\), the same column \(y\), or the same product \(xy\). Its size is the number of selected cells. The maximum size is denoted \(\tau(N_n)\). No ambient identity is adjoined, and no regularity assumption is imposed.

## Proof
**Upper bound.** Since \(0\) is a single product symbol, a partial transversal contains at most one cell with product \(0\). Let \(t\) be its number of nonzero-product cells. Each such cell has the form \((a^{i_h},a^{j_h})\) with \(i_h,j_h\ge1\) and \(s_h=i_h+j_h<n\). The \(t\) row exponents \(i_h\), the \(t\) column exponents \(j_h\), and the \(t\) sum exponents \(s_h\) are each pairwise distinct. Hence
\[
\sum_{h=1}^{t}s_h=\sum_{h=1}^{t}i_h+\sum_{h=1}^{t}j_h\ge t(t+1).
\]
Because the \(s_h\) are distinct and each lies in \(\{2,\ldots,n-1\}\), their total is at most the sum of the largest \(t\) positive integers not exceeding \(n-1\):
\[
\sum_{h=1}^{t}s_h\le tn-\frac{t(t+1)}{2}.
\]
For \(t\ge1\) it follows that \(3(t+1)\le2n\), or \(t\le\lfloor(2n-3)/3\rfloor\). The same last upper bound holds for \(t=0\) when \(n\ge2\). Adding at most one zero-product cell gives \(\tau(N_n)\le 1+\lfloor(2n-3)/3\rfloor=\lfloor2n/3\rfloor\).

**Attaining construction.** Put \(t=\lfloor(2n-3)/3\rfloor\). If \(t=0\), take the single cell \((0,0)\). Otherwise select \((0,0)\) together with \(t\) cells \((a^i,a^{\pi(i)})\) for \(1\le i\le t\), where \(\pi\) is the following explicit permutation of \(\{1,\ldots,t\}\).

If \(t=2k+1\) is odd, define
\[
\pi(i)=1+((i-1+k)\bmod(2k+1)).
\]
The \(t\) products have exponents \(i+\pi(i)\), which are exactly the consecutive integers \(k+2,k+3,\ldots,3k+2\). Indeed, the first \(k+1\) indices give alternating exponents \(k+2,k+4,\ldots,3k+2\), and the other \(k\) indices give \(k+3,k+5,\ldots,3k+1\). The definition of \(t\) implies \(3k+2\le n-1\), so all products are nonzero and distinct.

If \(t=2k\) is even, define \(\pi(i)\) to be the residue \(ki\bmod(2k+1)\), represented in \(\{1,\ldots,2k\}\). This is a permutation because \(\gcd(k,2k+1)=1\). For \(1\le j\le k\),
\[
\pi(2j-1)=k-j+1,\qquad \pi(2j)=2k+1-j.
\]
Consequently the odd rows give distinct sum exponents \(k+1,k+2,\ldots,2k\), while the even rows give \(2k+2,2k+3,\ldots,3k+1\). Again \(3k+1\le n-1\). Thus every product is distinct and nonzero. In either parity, rows and columns are distinct by construction. The added zero cell has a new row, column and product. This gives \(t+1=\lfloor2n/3\rfloor\) selected cells, proving equality.

## Verification
The standalone source `verification/check_monogenic_transversals.py` constructs the explicit witnesses and checks every row, column and product for \(2\le n\le70\). An independent exact dynamic-programming search over all nonzero-product cells confirms optimality for \(2\le n\le12\). The program prints `VERIFY_OK` on completion. These are finite corroborations; the unrestricted assertion is proved by the preceding inequalities and constructions.

## Relationship to prior work
A complete mapping of a semigroup gives a full transversal. Araújo, Bentz, Cameron, Hendrey and Kinyon study this existence problem for finite semigroups and prove that admitting a complete mapping requires regularity [1]. The present semigroups are nonregular for \(n\ge2\), so the qualitative obstruction is known; it does not determine the largest achievable *partial* transversal. The present theorem is an exact quantitative extremal result on a nilpotent family. Kinyon's earlier talk [2] develops the complete-mapping/full-transversal correspondence and regularity obstruction. Montgomery's survey [3] concerns partial transversals of Latin squares, where each symbol occurs once per row and column; a nilpotent semigroup table is not a Latin square. These distinctions do not assert that all older partial-transversal literature has been exhausted.

## Limitations
The formula applies specifically to nilpotent monogenic semigroups with the stated absorbing-zero multiplication, not arbitrary nilpotent or monogenic semigroups. It gives the maximum size and one family of witnesses, not a classification or enumeration of all optimal transversals. A potentially relevant 63-page recent paper [1] was available only through its abstract during the comparison; undiscovered equivalent results for truncated addition arrays remain a genuine novelty risk. This work has received a self-review but no independent mathematical audit.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092 (first posted 2026-08-25), https://arxiv.org/abs/2608.25092.
2. M. Kinyon, *Complete Mappings for Semigroups*, AGTA presentation, 2025-06-24, https://www.advgrouptheory.com/agta2025/Talks/Kinyon.pdf.
3. R. Montgomery, *Transversals in Latin Squares*, arXiv:2406.19873 (2024), https://arxiv.org/abs/2406.19873.
