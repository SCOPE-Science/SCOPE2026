# Exact capacity of binary \((2,3)\)-overlap-free codes

## Finding
For every integer \(n\ge6\), the maximum size of a binary \((2,3)\)-overlap-free code is
\[
S_2^3(2,n)=10\cdot2^{n-6}.
\]
The ten boundary patterns are optimal, not just maximal under inclusion. This determines the whole length range \(n\ge6\).

## Assumptions and scope
A binary word has exactly \(n\) bits. A code \(C\subseteq\{0,1\}^n\) is \((2,3)\)-overlap-free if, for every ordered pair \(x,y\in C\), including \(x=y\), and both \(j=2\) and \(j=3\), the first \(j\) bits of \(x\) differ from the last \(j\) bits of \(y\). No other overlap lengths, distance conditions, linearity, constant composition, or maximality assumption is imposed. The result covers \(n\ge6\), not shorter lengths or larger alphabets.

## Proof
**Boundary reduction.** Let \(P\) be the distinct three-bit prefixes and \(S\) the distinct three-bit suffixes of codewords. All pairs satisfy \(P\cap S=\varnothing\) (the length-three condition). Let \(B=\{p_{1}p_{2}:p\in P\}\) be the set of their length-two initial factors; the length-two condition is precisely that \(B\) be disjoint from the set of terminal length-two factors of \(S\). Conversely, any \(P,S\subseteq\{0,1\}^3\) satisfying these two disjointness conditions yield a valid code by concatenating \(p\), any \(n-6\) middle bits, and \(s\). Therefore
\[
S_2^3(2,n)=2^{n-6}\max_{P,S}|P||S|,
\]
where the maximum is over these disjointness conditions. Indeed, projection onto a six-bit prefix/suffix boundary has at most \(2^{n-6}\) preimages per boundary pattern, and all these preimages can be included simultaneously.

**Bounding the boundary product.** Put \(a=|P|\), \(b=|B|\), and let \(t\) count those three-bit words \(p\in P\) whose last two bits are *not* in \(B\). Every eligible suffix is outside \(P\) and has terminal two-bit factor outside \(B\). Hence
\[
|S|\le 2(4-b)-t.
\]
View each three-bit word \(uvw\) as a directed arc \(uv\to vw\) in the four-vertex binary De Bruijn graph. From each state there are two arcs, and the complete adjacency list is
```
00 -> 00, 01
01 -> 10, 11
10 -> 00, 01
11 -> 10, 11
```
In this notation \(a\le2b\), while \(a-t\) is at most the number of arcs internal to \(B\). An induced subset \(B\) of size one has at most one internal arc, and one of size two has at most two internal arcs: both facts follow immediately from the displayed four-state adjacency list (equivalently, check the four singleton and six two-vertex cases).

If \(b=1\), then \(a\le2\); when \(a=2\), the internal-arc cap gives \(t\ge1\), hence \(a|S|\le2(6-1)=10\); when \(a=1\), \(a|S|\le6\).

If \(b=2\), then \(a\le4\) and \(t\ge\max(0,a-2)\). Consequently
\[
a|S|\le a\bigl(4-\max(0,a-2)\bigr)\le9
\]
for the four possible positive integers \(a\le4\).

If \(b=3\), then \(a\le6\) and initially \(|S|\le2\), giving \(a|S|\le10\) for \(a\le5\). If \(a=6\), all outgoing arcs from \(B\) are in \(P\). The unique missing state receives an arc from \(B\): each missing state has an incoming predecessor different from itself, as the adjacency list shows. Thus \(t\ge1\), \(|S|\le1\), and \(a|S|\le6\).

If \(b=4\), no suffix has terminal pair outside \(B\), so \(S=\varnothing\). If \(P=\varnothing\), the product vanishes. In every case \(a|S|\le10\).

**Sharpness.** Choose the three-bit prefix set and suffix set
```
P = {000, 001}
S = {010, 011, 101, 110, 111}
```
They are disjoint and \(B=\{00\}\) is disjoint from all final two-bit factors in \(S\). Their Cartesian product gives ten distinct six-bit boundary words. Inserting each possible \(n-6\)-bit middle produces exactly \(10\cdot2^{n-6}\) codewords satisfying both forbidden-overlap conditions. This matches the bound.

## Verification
Run `python3 artifacts/verify.py` using the standard library. It enumerates all \(2^8=256\) three-bit prefix sets; computes their maximal admissible suffix sets independently of the analytic bound; verifies the exact maximum ten; checks the four-state induced-arc inequalities; checks the explicit boundary construction; and checks all ordered pairs of constructed words for lengths \(6,7,8\). Its output ends in `VERIFY_OK`. The finite enumeration is a reproducibility check, not a substitute for the displayed all-length proof.

## Relationship to prior work
Stanovnik (2024 preprint; 2025 article) proves a boundary-lifting identity for all \((t_1,t_2)\) restrictions, but its displayed exact maximum concerns \((1,2)\) and does not give the binary \((2,3)\) six-bit optimum. Yang and Ding (first public September 22, 2025) introduce general \((t_1,t_2)\) constructions and enumerate the sizes **of constructed families**, not the unrestricted maximum here. Blackburn–Nasr Esfahani–Kreher–Stinson (2022 preprint) prove exact optima for certain \((1,k)\) families, including \((1,3)\), which do **not** impose exactly the same forbidden-overlap lengths as \((2,3)\). The original distinction between restricted length intervals is essential. The present proof supplies a sharp extremal upper bound for the first two-consecutive-overlap interval that does not include length one.

## Limitations
No statement is made for lengths below six, alphabet sizes greater than two, or forbidden-overlap intervals other than exactly \(\{2,3\}\). There is no uniqueness or classification of all optimal codes. The proof assumes full freedom in the middle coordinates and does not impose error correction. An equivalent unindexed prior result remains possible; the short analytic argument and computational replay alone cannot establish publication novelty.

## References
1. L. Stanovnik, *Codes with restricted overlaps: expandability, constructions, and bounds*, arXiv:2411.02899, first posted November 5, 2024; Journal of Applied Mathematics and Computing (2025), doi:10.1007/s12190-025-02441-z.
2. H. Yang and Y. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, first publicly available September 22, 2025, doi:10.1587/transfun.2025EAL2050.
3. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher and D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, arXiv:2211.10309, first posted November 18, 2022.
4. Q. Cai, X. Wang and T. Feng, *Constructions and Bounds for q-Ary (1,k)-Overlap-Free Codes*, doi:10.1109/TIT.2023.3319010.
