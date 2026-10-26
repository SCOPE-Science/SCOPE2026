# Exact carry-automaton Abelian complexity of radix-\(k\) period-doubling shifts

## Finding
For every integer \(k\ge3\), the binary uniform substitution \(\varphi_k(0)=0^{k-1}1\) and \(\varphi_k(1)=0^k\) defines a primitive aperiodic minimal shift with a fixed point \(u\) starting at \(0\). Write \(\rho_k(n)\) for the number of distinct ones-counts among all length-\(n\) factors of \(u\). Every value \(\rho_k(n)\) is given exactly by a two-state signed-carry optimization requiring \(O(\log_k(n+1))\) integer operations. For all \(m\ge1\),
\[
\rho_k\!\left(\frac{k^{2m}-1}{k+1}\right)=m+1.
\]
Despite this unbounded Abelian complexity, every length \(k^m\) factor contains either \(\lfloor k^m/(k+1)\rfloor\) or \(\lceil k^m/(k+1)\rceil\) ones; both counts occur.

## Assumptions and scope
Fix \(k\ge3\) and \(n\ge1\). The sequence \(u=(u_j)_{j\ge0}\) is the one-sided fixed point of \(\varphi_k\), and its factors generate the standard two-sided minimal subshift. For \(N\ge0\), put \(S(N)=\sum_{j=0}^{N-1}u_j\). Write the unique finite radix expansion \(n=\sum_{j=0}^{h-1}a_jk^j\), where \(0\le a_j<k\), \(a_{h-1}>0\), and \(h\ge1\). An admissible carry sequence is a binary sequence \((c_j)_{j\ge0}\) with \(c_0=0\), finitely many nonzero entries, and, for every \(j\ge0\), a realizable addition of \(n\) to some nonnegative integer in which \(c_j\) is the incoming carry at radix position \(j\). For digits above \(h-1\), set \(a_j=0\). The weight of a carry sequence is
\[
W(c)=\sum_{j\ge1}(-1)^{j+1}c_j.
\]
The minimum and maximum of these weights over all admissible sequences are \(L_k(n)\) and \(H_k(n)\), respectively.

## Proof
**Valuation coding and exact prefix formula.** At an index \(j\equiv0,\ldots,k-2\pmod k\), the output is zero. At an index \(j=kr+k-1\), the output is \(1-u_r\). Therefore \(u_j\) equals the parity of the largest exponent \(v_k(j+1)\) for which \(k^{v_k(j+1)}\) divides \(j+1\). For every nonnegative \(N\),
\[
S(N)=\sum_{r\ge1}(-1)^{r+1}\left\lfloor \frac{N}{k^r}\right\rfloor,
\qquad
(k+1)S(N)-N=\sum_{j\ge0}(-1)^{j+1}d_j(N),
\]
where \(d_j(N)\) are the least-significant-first radix digits of \(N\). These finite identities follow because \(\mathbf1_{v\text{ odd}}=\sum_{r=1}^v(-1)^{r+1}\), and collecting the coefficient of each radix digit gives \((-1)^{j+1}\).

**Carry identity and exact optimization.** Addition of \(n\) to an arbitrary \(M\ge0\) has binary carries \(c_j\). If \(d_j(M+n)\) and \(d_j(M)\) are output and input digits, the column identity is \(d_j(M+n)-d_j(M)=a_j+c_j-kc_{j+1}\). Substituting into the preceding alternating-digit formula and telescoping gives
\[
S(M+n)-S(M)=S(n)+\sum_{j\ge1}(-1)^{j+1}c_j.
\]
At digit \(j\), a transition from incoming carry \(c\in\{0,1\}\) to outgoing carry \(c'\) can occur for some radix digit of \(M\) if and only if
\[
\begin{array}{ll}
c'=0:&a_j+c<k,\\
c'=1:&a_j+c>0.
\end{array}
\]
Indeed choosing the input digit \(0\) witnesses a permitted zero carry, and choosing \(k-1\) witnesses a permitted one carry; the reverse conditions follow from bounds on digits. Any finite path satisfying these conditions is realized by some finite integer \(M\). Thus minimizing or maximizing \(W(c)\) genuinely gives the extrema of all factor counts, with no relaxation or unproved compactness argument.

Here is the finite algorithm explicitly. Begin with a zero-valued state for \(c_0=0\) and an unreachable state for \(c_0=1\). For \(j=0,\ldots,h-1\), take all permitted transitions and add \((-1)^{j+2}c_{j+1}\) to the running minimum or maximum. At level \(h\), if \(c_h=0\), the tail adds zero. If \(c_h=1\), after the already-counted contribution from \(c_h\), the remaining carries at positions \(h+1,h+2,\ldots\) contribute either \(0\) or \((-1)^{h+2}\); both choices are realized by terminating the carry immediately or after one more step. Applying these two possible terminal corrections and taking the extrema gives \(L_k(n),H_k(n)\). There are two states per digit, so time is \(O(h)=O(\log_k(n+1))\).

As the starting position \(M\) increases by one, the number of ones in a length-\(n\) window changes by \(u_{M+n}-u_M\in\{-1,0,1\}\). Since both optimal counts are attained at finite starting positions, every integer between them is also attained. Therefore
\[
\boxed{\rho_k(n)=1+H_k(n)-L_k(n).}
\]

**Sharp logarithmic ladder.** Put \(n_m=(k^{2m}-1)/(k+1)\). Its base-\(k\) digits, from least significant upward, alternate \(k-1,0,k-1,0,\ldots,k-1\), ending at index \(2m-2\). The weight contribution of a carry at an odd index is positive and at an even index negative. Every even-index carry \(c_{2r}=1\) requires the preceding odd-index carry \(c_{2r-1}=1\), because the digit at index \(2r-1\) is zero. Consequently the total carry weight is nonnegative. It is at most \(m\), since only \(m\) positive-index positions appear up through the last active radix digit, and the eventual high-digit carry tail cannot increase their contribution. The lower bound zero is reached at \(M=0\); the upper bound \(m\) is attained at \(M=\sum_{r=0}^{m-1}k^{2r}\), which creates one positive carry after each digit \(k-1\), then terminates it at the next zero digit. Hence \(L_k(n_m)=0\), \(H_k(n_m)=m\).

**Perfect substitution-scale balance.** For \(n=k^m\), all lower \(m\) radix digits vanish, forcing all lower carries to vanish. The first possible carry is at index \(m+1\), and its tail makes the total weight either \(0\) or \((-1)^{m+2}\); both possibilities occur. Since \(k\equiv-1\pmod{k+1}\), substituting into the carry identity yields precisely the two adjacent integers \(\lfloor k^m/(k+1)\rfloor\) and \(\lceil k^m/(k+1)\rceil\).

Finally \(\varphi_k^2\) sends each letter to a word containing both letters, so the substitution is primitive. The exact radix prefix formula gives unbounded discrepancy from frequency \(1/(k+1)\), by choosing digits \(k-1\) at many alternating positions; this excludes periodicity. Thus the associated shift is indeed aperiodic and minimal.

## Verification
The accompanying `verify.py` independently constructs finite substitution prefixes, compares them with the valuation-parity characterization, checks the exact digit-prefix identity, computes carry extrema for every length up to \(79\) in radices \(2\) through \(6\), and compares these extrema with brute-force sliding-window counts. It also checks the logarithmic-ladder and substitution-scale cases in finite ranges. All **85,483** exact-integer assertions passed. The binary radix \(2\) is included as a prior-work control, not claimed as new. The proof above, not this bounded computation, establishes the theorem for every \(k\ge3\), every length, and every exponent.

## Relationship to prior work
Berthé, Cecchi-Bernales and Espinoza study letter balance and coboundaries of primitive substitutive subshifts, including the classical binary period-doubling substitution, and give a general qualitative criterion. Parreau, Rigo, Rowland and Vandomme analyze Abelian and higher Abelian complexity in the ordinary radix-two period-doubling setting; the entire radix-two case, including prior recurrence phenomena, is excluded from the novelty claim. Bognini and Ammar study a different `k`-letter, length-two period-doubling generalization, not the present binary length-\(k\) substitution. The exact two-state radix-addition formula and all-length Abelian-complexity classification for \(k\ge3\), together with the explicit unbounded ladder and exact-scale balance, are the asserted specialization. General digit-arithmetic and automatic-sequence techniques are established background, not themselves new.

## Limitations
The result concerns a specified uniform binary substitution for integer radix \(k\ge3\), not all primitive substitutions, arbitrary odometer factors, higher-order Abelian complexities, or weighted letter potentials. The logarithmic ladder provides exact values along one infinite subsequence, not a closed elementary formula for every length; the latter is provided by the finite carry algorithm. Historical priority for equivalent high-radix carry formulations remains uncertain.

## References
1. V. Berthé, P. Cecchi-Bernales, B. Espinoza, *Continuous eigenvalues of minimal subshifts via S-adic representations and coboundaries*, arXiv:2602.04833 (first posted 2026-02-04), especially §§6.1 and 9.1; https://arxiv.org/abs/2602.04833.
2. A. Parreau, M. Rigo, E. Rowland, É. Vandomme, *A new approach to the \(2\)-regularity of the \(\ell\)-abelian complexity of \(2\)-automatic sequences*, Electronic Journal of Combinatorics 22 (2015), P1.27; arXiv:1405.3532, https://arxiv.org/abs/1405.3532.
3. K. E. Bognini, H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881 (2025); https://arxiv.org/abs/2511.20881.
4. G. Richomme, K. Saari, L. Q. Zamboni, *Abelian complexity of minimal subshifts*, Journal of the London Mathematical Society 83 (2011), 79–95, doi:10.1112/jlms/jdq063.
