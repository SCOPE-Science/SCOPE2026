# Exact twelve-step prefix-extremum law for modulo-seven Thue–Morse sums

## Finding
For every nonnegative integer \(n\), let \(t(n)=(-1)^{s_2(n)}\), where \(s_2(n)\) is its binary digit sum, and set
\[
D_7(N)=\sum_{0\le n<N,\;7\mid n}t(n).
\]
For each integer \(r\ge0\), put
\[
U_r=\max_{0\le N\le2^r}D_7(N),\qquad
L_r=\min_{0\le N\le2^r}D_7(N).
\]
**Theorem.** For every integer \(r\ge7\),
\[
U_{r+12}=49U_r+32,\qquad L_{r+12}=49L_r-32.
\]
More strongly, the same identities hold for each residue modulo seven when the sum ranges over indices in that residue class (see the proof). In particular, for every integer \(k\ge0\),
\[
U_{12k+7}=\frac{5\cdot49^k-2}{3},\qquad
L_{12k+7}=\frac{2-29\cdot49^k}{3}.
\]
With \(\alpha=\log_2(7)/6\), one has \(D_7(N)=O(N^\alpha)\) and
\[
-\infty<\liminf_{N\to\infty}\frac{D_7(N)}{N^\alpha}<0
<\limsup_{N\to\infty}\frac{D_7(N)}{N^\alpha}<\infty.
\]
The quantitative exponent is contextual, not asserted to be new independently of the known spectral/fractal literature; the new asserted theorem is the exact additive twelve-level extremum recursion.

## Assumptions and scope
All indices \(n,N,r,k\) are ordinary nonnegative integers, and the residue modulus is exactly seven. The extrema include the empty prefix \(N=0\) and the full prefix \(N=2^r\). No periodicity, analytic continuation, or probabilistic hypotheses are assumed. The recurrence is stated for all levels \(r\ge7\), not for all smaller levels.

## Proof
For \(j\in\{0,1,2,3,4,5,6\}\), let
\[
D_{r,j}(N)=\sum_{\substack{0\le n<N\\n\equiv j\pmod7}}t(n)
\quad(0\le N\le2^r).
\]
Write \(T_{r,j}=D_{r,j}(2^r)\), \(H_{r,j}=\max_N D_{r,j}(N)\), and \(B_{r,j}=\min_N D_{r,j}(N)\). At depth zero, \(T_{0,0}=H_{0,0}=1\), while all other \(T_{0,j},H_{0,j}\) and every \(B_{0,j}\) vanish.

Let \(\delta_r\equiv2^r\pmod7\). The second half of a length-\(2^{r+1}\) Thue–Morse block is the sign-reversed first half, with residues shifted by \(\delta_r\). Consequently (all residue subscripts are reduced modulo seven),
\[
\begin{aligned}
T_{r+1,j}&=T_{r,j}-T_{r,j-\delta_r},\\
H_{r+1,j}&=\max\{H_{r,j},\;T_{r,j}-B_{r,j-\delta_r}\},\\
B_{r+1,j}&=\min\{B_{r,j},\;T_{r,j}-H_{r,j-\delta_r}\}.
\end{aligned}
\tag{1}
\]
This is an exact identity for all possible prefixes, because any prefix either lies wholly in the first half or consists of that half followed by a prefix of the sign-reversed second half.

Iterating (1) with integers for exactly nineteen levels gives this complete seven-residue finite certificate. Each parenthesized vector lists residue coordinates in order \(0,1,\ldots,6\):

| Level | \(T\) | \(H\) | \(B\) |
|---|---|---|---|
| \(r=7\) | \((-7,7,0,0,0,0,0)\) | \((1,8,3,4,1,4,3)\) | \((-9,-2,-1,0,-3,0,-1)\) |
| \(r=19\) | \((-343,343,0,0,0,0,0)\) | \((81,424,179,228,81,228,179)\) | \((-473,-130,-81,-32,-179,-32,-81)\) |

Coordinatewise, this certifies
\[
T_{19,j}=49T_{7,j},\qquad H_{19,j}=49H_{7,j}+32,\qquad B_{19,j}=49B_{7,j}-32.
\tag{2}
\]
The integer-only verifier independently regenerates this table and compares the recurrence with direct digit-sum enumeration through level sixteen. The certificate is therefore finite and completely reproducible, rather than an inference from experiments about larger depths.

Because \(2^3\equiv1\pmod7\), the shifts obey \(\delta_{r+12}=\delta_r\). If the triple at level \(r+12\) is obtained from the triple at level \(r\) via the affine transformation
\[
(T,H,B)\longmapsto(49T,\;49H+32,\;49B-32),
\]
then (1) gives the same relation at levels \(r+13\) and \(r+1\): multiplication by positive \(49\) commutes with maxima and minima, while both candidate expressions acquire exactly the same additive constant. Thus the affine transformation commutes with every applicable one-level transition. Induction from (2) proves it for every \(r\ge7\). Taking residue \(j=0\) gives the theorem.

The depth-seven values are \(U_7=1\) and \(L_7=-9\); solving the first-order twelve-step recurrences gives the closed formulas for \(U_{12k+7}\) and \(L_{12k+7}\). For each fixed residue class \(a\pmod{12}\) and all sufficiently large \(r\equiv a\), the affine recursion implies \(H_{r,0},-B_{r,0}=O(49^{r/12})\). For \(2^{r-1}<N\le2^r\), this yields \(|D_7(N)|=O(N^\alpha)\), since \(49^{r/12}=2^{r\alpha}\). Every extremum is attained by an integer prefix. Since the positive and negative closed-form extrema both grow on the order of \(49^k\), the maximizing and minimizing prefixes diverge, have length at most \(2^{12k+7}\), and respectively yield normalized values bounded away from zero with opposite signs. The global normalized upper and lower limits are finite by the uniform bound. This completes the proof.

## Verification
Execute `python3 verify.py` with Python 3.8 or newer. The script uses only the Python standard library. It checks (1) against every prefix for all seven residues through depth sixteen; it computes the depth-seven and depth-nineteen certificate vectors from the zero-depth initialization; and it checks all seven-coordinate affine equalities for many further depths, the latter only as supplementary testing. Its displayed `VERIFY_OK` message does not substitute for the induction proving all depths.

## Relationship to prior work
Goldstein, Kelly and Speer (1992) studied general \(p\)-rarefied Thue–Morse partial sums through self-similar fractal approximations and determined spectral growth rates in situations including modulus seven. Their growth-order framework is **not** claimed as new. The asserted distinction is the completely **exact integer affine law for extrema over every finite dyadic prefix window**, including both signs, the additive constants \(\pm32\), its certified starting depth, and all seven residue classes. This finite-window extremum law does not follow merely from knowing a leading growth exponent or a fractal approximation with nonzero error.

Drmota and Skałba (1999/2000) analyzed rarity and sign phenomena for rarefied sums, principally when the modulus is divisible by three or has the form \(4^j+1\). Drmota and Stoll (2004/2008) developed generalized Newman phenomena; their inspected full-text discussion states positivity and eventual-sign properties and does not give the exact modulus-seven prefix-extremum law. Shallit (2023) studied related rarefied sums using automata and logic, with detailed modulus-three and modulus-five instances but not this modulus-seven exact extrema formula.

## Limitations
The full text of the highly relevant 1992 Goldstein–Kelly–Speer paper was not accessible; its abstract documents strong prior spectral/fractal coverage, and exact-extremum priority within its interior cannot be ruled out. The 1999 Drmota–Skałba full text was also not accessible, despite attempts at open and authorized routes. Accordingly independent priority review is warranted. The proof establishes only modulus seven and dyadic-prefix maxima/minima, and does not determine the exact normalized limsup or liminf constants. No independent audit or external mathematical certification has been performed.

## References
1. S. Goldstein, K. A. Kelly, E. R. Speer, “The fractal structure of rarefied sums of the Thue–Morse sequence,” *Journal of Number Theory* 42 (1992), 1–19. DOI: 10.1016/0022-314X(92)90104-W.
2. M. Drmota, M. Skałba, “Rarified sums of the Thue–Morse sequence,” *Transactions of the American Mathematical Society* 352 (2000), 609–642. DOI: 10.1090/S0002-9947-99-02277-1.
3. M. Drmota, T. Stoll, “Newman’s phenomenon for generalized Thue–Morse sequences,” manuscript dated 25 November 2004; *Discrete Mathematics* 308 (2008), 1191–1208. https://www.dmg.tuwien.ac.at/drmota/newman.pdf.
4. J. Shallit, “Rarefied Thue-Morse Sums Via Automata Theory and Logic,” arXiv:2302.09436 (2023). https://arxiv.org/pdf/2302.09436.
5. D. J. Newman, “On the number of binary digits in a multiple of three,” *Proceedings of the American Mathematical Society* 21 (1969), 719–721.
