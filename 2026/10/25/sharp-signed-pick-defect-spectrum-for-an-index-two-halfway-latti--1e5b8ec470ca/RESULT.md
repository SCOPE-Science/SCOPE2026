# Sharp signed Pick-defect spectrum for an index-two halfway-lattice triangle family

## Finding

For every odd integer \(b\ge3\) and every integer \(k>(b+1)/2\), define
\[
T_{b,k}=\{(x,y)\in\mathbb R^2:x\ge\tfrac12,\ y\ge\tfrac12,\ 2x+by\le k+\tfrac12\},
\qquad \Delta_{b,k}=\operatorname{area}(T_{b,k})-\#(\operatorname{int}T_{b,k}\cap\mathbb Z^2).
\]
Write \(k=bq+r\), where \(q\ge0\) and \(0\le r<b\). Then
\[
\boxed{\Delta_{b,k}=\frac{(2r-b-1)^2}{16b}+\begin{cases}
0& q\text{ even},\\[-2pt]
-\tfrac14& q\text{ odd and }r\text{ even},\\[-2pt]
\tfrac14& q\text{ odd and }r\text{ odd}.
\end{cases}}
\]
For fixed \(b\), its *exact attained* minimum and maximum over all admissible integers \(k\) are
\[
\boxed{\min\Delta_{b,k}=\begin{cases}-\tfrac14&b\equiv3\pmod4,\\[-2pt] -\frac{b-1}{4b}&b\equiv1\pmod4,\end{cases}
\qquad \max\Delta_{b,k}=\frac{(b+1)^2}{16b}.}
\]
The minimum occurs precisely at odd \(q\) with \(r=(b+1)/2\) when \(b\equiv3\pmod4\), and at odd \(q\) with \(r=(b+1)/2-1\) or \(r=(b+1)/2+1\) when \(b\equiv1\pmod4\). The maximum occurs precisely at even \(q\) with \(r=0\), or odd \(q\) with \(r=1\), whenever \(k>(b+1)/2\). Finally,
\[
\boxed{\Delta_{b,k}<0\iff q\text{ odd},\ r\text{ even},\ \lvert2r-b-1\rvert<2\sqrt b.}
\]
Hence only \(O(\sqrt b)\) of the \(2b\) residue classes have negative discrepancy, whereas the largest positive discrepancy is of order \(b\). In particular \(-1/4\) is a uniform sharp lower bound across the whole family, attained for every \(b\equiv3\pmod4\).

## Assumptions and scope

All lattice points are counted in the *interior* of \(T_{b,k}\). The triangle is nondegenerate because \(k>(b+1)/2\). Its three facet normals may be taken as \((1,0)\), \((0,1)\), and \((-2,-b)\); each is primitive because \(b\) is odd and each facet lies at a half-integer support level. Thus each facet contains no integral lattice point. The absolute determinants of consecutive primitive facet normals are \(1\), \(2\), and \(b\), so these examples are outside the all-unimodular hypothesis for \(b\ge3\). No claim is made for arbitrary nonunimodular halfway-lattice polygons.

## Proof

Put \(d=k-(b+1)/2>0\). Translating the lower-left vertex \((1/2,1/2)\) to the origin gives a right triangle with horizontal leg \(d/2\) and vertical leg \(d/b\). Consequently
\[
\operatorname{area}(T_{b,k})=\frac{(k-(b+1)/2)^2}{4b}=\frac{(2k-b-1)^2}{16b}.
\]
Because no edge contains lattice points, an integer point in the triangle has \(x,y\ge1\) and satisfies \(2x+by\le k\). With \(k=bq+r\), the number for row \(y\) is \(\lfloor(k-by)/2\rfloor\) when positive; including its zero values yields the *exact* finite count
\[
I_{b,k}=\sum_{y=1}^{q}\left\lfloor\frac{k-by}{2}\right\rfloor
=\sum_{j=0}^{q-1}\left\lfloor\frac{bj+r}{2}\right\rfloor.
\]
This formula remains valid for \(q=0\), when the sum is empty and there are no interior lattice points. Since \(b\) is odd, the parity of \(bj+r\) equals that of \(j+r\). Let \(E\) count odd terms among \(j+r\) for \(0\le j<q\). Then
\[
I_{b,k}=\frac{bq(q-1)}4+\frac{qr}{2}-\frac{E}{2},\qquad
E=\begin{cases}q/2&q\text{ even},\\ (q-1)/2&q\text{ odd},\ r\text{ even},\\ (q+1)/2&q\text{ odd},\ r\text{ odd}.\end{cases}
\]
Substitution of \(k=bq+r\) in the area formula and subtraction of \(I_{b,k}\) cancels every positive-degree term in \(q\), leaving the displayed exact discrepancy. Thus the full discrepancy is periodic in \(k\) with period \(2b\) on the admissible domain.

For the minimum, the even-\(q\) branch is nonnegative, whereas the odd-\(q\), odd-\(r\) branch is at least \(1/4\). On the odd-\(q\), even-\(r\) branch, minimization is exactly minimization of \((2r-b-1)^2\) over even \(0\le r<b\). If \(b\equiv3\pmod4\), \((b+1)/2\) is even and the square can vanish, yielding \(-1/4\). If \(b\equiv1\pmod4\), \((b+1)/2\) is odd and the two nearest permitted even remainders give square \(4\), yielding \(1/(4b)-1/4=-(b-1)/(4b)\). Both branches give strictly negative values for \(b\ge3\), so these are the global minima and the stated equality classes are exhaustive.

For the maximum, on the even-\(q\) branch the absolute value \(\lvert2r-b-1\rvert\) is at most \(b+1\), with equality only at \(r=0\). On the odd-\(q\), even-\(r\) branch it is also at most \(b+1\), but the additional \(-1/4\) makes the result strictly below \((b+1)^2/(16b)\). On the odd-\(q\), odd-\(r\) branch, \(1\le r\le b-2\); therefore \(\lvert2r-b-1\rvert\le b-1\), with equality only at \(r=1\), and \((b-1)^2/(16b)+1/4=(b+1)^2/(16b)\). These are all maximizing cases. The sign criterion follows immediately by comparing the squared term to \(1/4\) on the only potentially negative branch. Its interval of allowed even remainders has length less than \(2\sqrt b\) and therefore contains \(O(\sqrt b)\) candidates.

## Verification

The accompanying standalone \(\texttt{verification/check.py}\) uses exact rational arithmetic, directly counts integer points row by row, compares the closed expression, checks the sign condition and both sharp bounds, and independently identifies equality residues. It exhaustively tests all odd \(b\) from \(3\) to \(121\) and all admissible \(k\) up to \(7b\), as well as full residue cycles. It is supporting finite evidence; the proof above covers all allowed integers without relying on enumeration.

## Relationship to prior work

Chu and Karshon prove a Pick-type identity for *unimodular* halfway-lattice polygons; their triangle case gives constant area-minus-interior-count \(1/8\). The present facet-normal determinants \(1,2,b\) violate that hypothesis, and the discrepancy instead has a sharp signed periodic spectrum. Beck and Robins provide general Dedekind–Rademacher formulas for lattice points in rational polygons and thus a general algorithm able to compute individual members of this family. The present result is a direct family-wide simplification and optimization of the signed defect, with sharp parameter-uniform bounds, complete equality cases and the narrow negative window; these statements are not claimed to be inaccessible through specialization of general counting methods.

## Limitations

This is a theorem for the explicitly defined two-parameter family only, not a general Pick theorem for nonunimodular polygons. The new feature is the uniform signed extremal and phase analysis, rather than the existence of lattice-point counting algorithms. Absolute literature priority remains unverified: a previously published specialization or corollary could encompass the same uniform extremum. The finite checker is not a proof of the all-parameter assertion.

## References

1. Charlene Chu and Yael Karshon, *A Pick-type theorem for halfway-lattice polygons* (2026), arXiv:2610.00696v1, https://arxiv.org/html/2610.00696v1.
2. Matthias Beck and Sinai Robins, *Explicit and efficient formulas for the lattice point count in rational polygons using Dedekind–Rademacher sums* (2001 preprint), arXiv:math/0111329v2, https://arxiv.org/html/math/0111329v2.
