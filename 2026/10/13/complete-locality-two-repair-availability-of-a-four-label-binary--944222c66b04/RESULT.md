# Complete locality-two repair availability of a four-label binary spread code

## Finding

The spread-labelled evaluation code specified by Example 1 of Sarkar–Hansda–Maji has all-symbol repair locality exactly \(2\). Its \(255\) coordinates have the **complete two-helper availability distribution**
\[
 \#\{x: t(x)=a\}=
 \begin{cases}
 30 & a=3,\\
 30 & a=4,\\
 60 & a=6,\\
 15 & a=7,\\
 30 & a=8,\\
 30 & a=9,\\
 60 & a=12,\\
 0 & \text{otherwise.}
 \end{cases}
\]
Here \(t(x)\) is the maximum number of pairwise disjoint sets of at most two other coordinates which, over the binary field, recover the symbol at coordinate \(x\). All such two-helper sets through a fixed target are intrinsically pairwise disjoint. Across all targets, they arise from exactly \(635\) distinct weight-three dual supports (and hence \(3\cdot635=1905\) target–helper-pair incidences). These conclusions are independent of the particular full binary spread realizing the prescribed index pattern.

For the defining index sets *as printed* in the source, the same code has exact parameters \([255,12,60]_2\). In particular, its minimum distance is \(60\), not \(75\) as assigned to that example in the source. This parameter qualification is necessary when interpreting the recovery profile as an error-resilience statement.

## Assumptions and scope

Let \(m\ge2\), \(V=\mathbb F_2^{2m}\), and let \(V_1,\ldots,V_{2^m+1}\) be a **full** \(m\)-spread: every \(V_i\) is an \(m\)-dimensional subspace, distinct members intersect only at \(0\), and their nonzero elements partition \(V\setminus\{0\}\). Give each spread member an arbitrary label \(b_i\in\mathbb F_2^s\). At every nonzero \(x\in V_i\), form the binary generator column \(g_x=(x,b_i)\in\mathbb F_2^{2m+s}\); let \(C\) be the row span of these columns. The theorem below concerns linear recovery by at most two other *distinct* coordinates, and assumes no repeated coordinate positions.

For \(x\in V_i\setminus\{0\}\), the exact number of distinct two-helper repair sets is
\[
 t_i=(2^{m-1}-1)\mathbf 1_{b_i=0}
   +\#\bigl\{\{j,k\}:1\le j<k\le 2^m+1,\ j,k\ne i,\ b_j+b_k=b_i\bigr\}.
\]
Every qualifying set is disjoint from every other qualifying set. The formula applies to arbitrary labels, regardless of the dimension of the resulting code, and is invariant under changing the full spread while retaining its index labels.

Specialize to \(m=4\), \(s=4\), with the four indicator-function index sets (indexed from \(1\) to \(17\))
\[
\begin{aligned}
 S_1&=\{1,2,3,4,10,11,13\},\\
 S_2&=\{3,4,5,6,10,11,13\},\\
 S_3&=\{1,3,7,8,10,12,13\},\\
 S_4&=\{2,3,5,9,11,12,13\},
\end{aligned}
\]
where \(b_i=(\mathbf 1_{i\in S_1},\ldots,\mathbf 1_{i\in S_4})\). The profile of \(t_i\) for indices \(1,\ldots,17\) is
\[
 (4,3,9,6,4,3,8,8,6,6,7,6,9,12,12,12,12).
\]
Each entry applies to all \(15\) coordinates in its spread member. This is the exact local-recovery statement, not a claim that all \(255\) coordinates have the same availability.

## Proof

**All possible repair pairs.** A binary linear recovery relation from a helper pair \(\{y,z\}\) to \(x\) holds for every codeword precisely when \(g_x+g_y+g_z=0\). This follows because a vector supported on the three positions belongs to the orthogonal (dual) code exactly when it annihilates the generator matrix. Its first \(2m\) entries force \(x+y+z=0\). There are no zero columns or duplicated columns: distinct \(x\) have distinct nonzero first blocks. Thus there is no one-helper recovery.

If two of \(x,y,z\) belong to the same spread member, all three belong to that member; the label condition is \(3b_i=b_i=0\). For a fixed nonzero \(x\in V_i\), every \(y\in V_i\setminus\{0,x\}\) gives \(z=x+y\); unordered pairs number \((2^m-2)/2=2^{m-1}-1\). Otherwise the three members \(i,j,k\) are pairwise distinct. Since \(V_j\cap V_k=\{0\}\) and \(\dim(V_j)+\dim(V_k)=2m\), every \(x\in V_i\setminus\{0\}\) decomposes uniquely as \(x=y+z\) with \(y\in V_j\), \(z\in V_k\). Neither summand is zero, since \(V_i\) meets neither \(V_j\) nor \(V_k\) outside \(0\). The label condition is exactly \(b_i+b_j+b_k=0\), proving the formula and exhaustiveness. For a fixed \(x\), a helper \(y\) determines \(z=x+y\) uniquely. Hence no two distinct qualifying pairs share a helper, so their number is the maximum two-helper disjoint availability.

**Numerical label census.** Encode four-bit labels by bit positions corresponding to \(S_1,S_2,S_3,S_4\). Then
\[
 (b_1,\ldots,b_{17})=(5,9,15,3,10,2,4,4,8,7,11,12,15,0,0,0,0).
\]
Exactly \(33\) unordered triples of distinct member indices have zero XOR of their labels, and exactly \(4\) member labels vanish. Counting the triples containing each index and adding \(7\) internal repair pairs for a zero label gives the displayed \(t_i\)-vector. The histogram follows by multiplying the index counts by \(15\). Each zero-sum triple of distinct spread members contributes \(15\) different dual-weight-three relations, one for each nonzero \(x\) in any fixed one of the members. Each zero-labelled member contributes \((15\cdot14)/6=35\) internal triples. Therefore the total is \(33\cdot15+4\cdot35=635\). This count is also consistent with \(\sum_x t(x)=3\cdot635\).

**Dimension and distance, including the boundary value.** For any \(\alpha\in\mathbb F_2^4\), let \(u(\alpha)=\#\{i:\alpha\cdot b_i=1\}\). Its values as \(\alpha\) ranges over nonzero four-bit vectors are \(4,6,7,8,9\), and \(u(3)=4\). The codewords have the form \((\alpha\cdot b_{i(x)}+\ell(x))_{x\ne0}\), with \(\ell\) an arbitrary binary linear functional on \(V\). If \(\alpha=0,\ell\ne0\), the weight is \(128\). If \(\alpha\ne0,\ell=0\), the weight is \(15u(\alpha)\). For nonzero \(\ell\), the orthogonal complements \(V_i^\perp\) themselves form a full spread, so \(\ell\) is zero on exactly one of the \(V_i\). The standard character sum on each \(V_i\) gives weight \(144-u(\alpha)\) if that index is selected by \(\alpha\), and \(128-u(\alpha)\) otherwise. All these weights are at least \(60\); equality is attained by \(\ell=0\) and \(\alpha=3\), whose support is precisely the four spread members indexed by \(S_1\triangle S_2=\{1,2,5,6\}\). No nonzero parameter combination gives a zero codeword, so the generator has rank \(12\) and the minimum distance is \(60\).

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The program builds the Desarguesian full spread of \(\mathbb F_{16}^2\), using the irreducible polynomial `0x13`, constructs all \(255\) columns, computes the rank of the \(12\) generator rows, enumerates all \(4096\) codewords by Gray code, and enumerates all zero-sum distinct column triples. It separately computes the repair profile from the \(17\) index labels without using the field construction, checks that all repair pairs at each coordinate are disjoint, and verifies \(635\), the histogram, the exact dimension, and the distance. A successful run ends with `VERIFY_OK`. Finite enumeration certifies the explicitly constructed spread instance; the preceding algebraic proof establishes spread-independence.

## Relationship to prior work

Sarkar, Hansda, and Maji introduced these four spread-indicator functions and studied the resulting code's weights, minimality and secret-sharing access structures. Their Example 1 is the source of the four index sets, not a source for the local-repair profile proved here. The claimed distance \(75\) is not compatible with the printed index sets, since \(S_1\triangle S_2\) consists of four spread members and supplies a weight-\(60\) codeword. The proof above independently rules out smaller weights.

Huang and colleagues, Ma and Ge, and the literature on binary codes with uneven availability establish locality-two repair and multiple disjoint recovery sets in other constructions. In particular, Ma and Ge obtain length-three local groups using parity-check designs based on partial spreads, whereas the present generator-column model has \(255\) projective positions and label-dependent triple relations. A separate affine-half extension of partial-spread Boolean codes deliberately duplicates coordinates (and has dual distance \(2\)), so it does not imply the present projective local-repair profile. The number of all weight-three dual words, even if derived from a complete weight enumerator through the MacWilliams transform, does not by itself specify the seven class sizes of the **coordinatewise** availability spectrum.

## Limitations

The exact histogram concerns the published four index sets and full binary four-spreads, not arbitrary partial spreads, altered label assignments, or nonbinary fields. The general counting formula covers arbitrary labels on full binary spreads but gives no unexplored global optimum among competing codes. Availability is restricted to disjoint recovery sets of size at most \(2\); larger repair groups and more general failure models are not classified. Any stronger claim about minimality or the published access structure would require separate analysis. The originality comparison is limited by the literature accessed, and independent mathematical audit has not been performed.

## References

1. A. Sarkar, K. Hansda and M. Maji, *Minimal Binary Linear Codes of Dimension n+4 from Partial Spreads and Their Dual Access Structures*, arXiv:2608.04889v1 (first public 2026-08-05), especially Section 3 and Example 1.
2. P. Huang, E. Yaakobi, H. Uchikawa and P. H. Siegel, *Binary Linear Locally Repairable Codes*, IEEE Transactions on Information Theory 62 (2016), 6268–6283; available as a 2015 preprint.
3. J. Ma and G. Ge, *Optimal Binary Linear Locally Repairable Codes with Disjoint Repair Groups*, arXiv:1711.07138v1 (2017), particularly Sections II and IV (2019 journal version, DOI: 10.1137/19M1248443).
4. *New Binary Locally Repairable Codes with Locality 2 and Uneven Availabilities for Hot Data*, Entropy 20 (2018), article 636, DOI: 10.3390/e20090636.
5. J.-H. Chung, D. Jin and D. Kim, *Affine-Half Extensions of Partial-Spread Minimal Binary Linear Codes with Explicit Weight Distributions*, Mathematics 14 (2026), article 3152, DOI: 10.3390/math14173152.
