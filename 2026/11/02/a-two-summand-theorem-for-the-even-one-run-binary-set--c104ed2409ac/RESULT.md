# A two-summand theorem for the even-one-run binary set

## Finding
Let \(\mathcal E\) consist of \(0\) and all positive integers whose ordinary binary expansions have **even length for every maximal run of consecutive ones**. Then
\[
\boxed{\mathcal E+\mathcal E=3\mathbb Z_{\geq0}}.
\]
Equivalently, **every nonnegative multiple of three** is the sum of two (possibly zero) integers having only even-length one-runs in binary; no integer outside the multiples of three has such a representation. Consequently \(\mathcal E/3=\{e/3:e\in\mathcal E\}\) is an additive basis of exact order two for the nonnegative integers. The order is minimal because \(9\notin\mathcal E\), while \(9=3+6\) with \(3,6\in\mathcal E\).

## Assumptions and scope
A maximal one-run is a maximal nonempty block of ones in the canonical base-two expansion; its length counts the consecutive ones. The integer \(0\) is included with an empty list of runs. The sumset uses nonnegative summands and permits equal summands and the summand \(0\). The assertion holds for **all** nonnegative integers, without a cutoff. It does not assert positive summands for the smallest targets or a uniqueness statement.

## Proof
First, each block of \(2j\) consecutive ones, beginning at bit position \(h\), contributes \(2^h(2^{2j}-1)\). This integer is divisible by three. Since distinct maximal blocks contribute additively, each element of \(\mathcal E\) is divisible by three; hence \(\mathcal E+\mathcal E\subseteq3\mathbb Z_{\geq0}\).

For the reverse inclusion, construct a nondeterministic digit automaton recognizing exactly \(\mathcal E+\mathcal E\). Read the binary digits of the proposed sum from least significant to most significant. An automaton state is \((u,v,c)\in\{0,1\}^3\): \(u\) and \(v\) are the current parities of the one-runs in the two proposed summands, and \(c\) is their incoming binary carry. The initial and only accepting state is \((0,0,0)\). For a chosen summand digit \(a\in\{0,1\}\), define the parity update \(H(u,a)\) by \(H(u,1)=1-u\), \(H(0,0)=0\), with \(H(1,0)\) undefined. The undefined case forbids closing a one-run of odd length. For a proposed output bit \(b\), choose input digits \(a,d\in\{0,1\}\) with \(a+d+c\equiv b\pmod2\), require both parity updates to be defined, and move to
\[
\bigl(H(u,a),H(v,d),\lfloor(a+d+c)/2\rfloor\bigr).
\]
This precisely encodes binary addition and the even-run constraint. Acceptance after the final output bit requires both completed runs to be even and the carry to be zero. Thus a finite binary word is accepted precisely when its numerical value belongs to \(\mathcal E+\mathcal E\). Leading zero padding presents no difficulty.

To prove that the automaton accepts **every** multiple of three, determinize it via the reachable set of nondeterministic states. Track simultaneously the residue \(r\in\{0,1,2\}\) of the already-read number and the position parity \(p\in\{0,1\}\) of the next binary digit. Reading bit \(b\) updates \(r\) to \(r+(-1)^p b\pmod3\) and \(p\) to \(1-p\), since \(2\equiv-1\pmod3\). A direct complete reachability calculation produces exactly the following **ten** configurations. The triples in the subset column represent \((u,v,c)\); transitions are under next bits \(0\) and \(1\):

| State | Nondeterministic subset | \(r\) | \(p\) | Next 0 | Next 1 |
|---:|---|---:|---:|---:|---:|
| 0 | 000 | 0 | 0 | 1 | 2 |
| 1 | 000, 111 | 0 | 1 | 3 | 4 |
| 2 | 010, 100 | 1 | 1 | 5 | 0 |
| 3 | 000, 111 | 0 | 0 | 1 | 6 |
| 4 | 001, 010, 100 | 2 | 0 | 7 | 1 |
| 5 | 011, 101 | 1 | 0 | 8 | 7 |
| 6 | 001, 010, 100 | 1 | 1 | 5 | 3 |
| 7 | 011, 101 | 2 | 1 | 9 | 5 |
| 8 | 001 | 1 | 1 | 5 | 3 |
| 9 | 001 | 2 | 0 | 7 | 1 |

State 0 is initial. Every transition in the table follows by checking the four possible pairs of summand digits. The table is closed under both inputs, so **no other configurations are reachable**. The accepting nondeterministic state \(000\) occurs in a subset **exactly in rows 0, 1, and 3**, all and only the rows with residue \(r=0\). Therefore a finite input word is accepted if and only if its value is divisible by three. This proves the reverse inclusion and the sumset identity for arbitrarily long binary inputs. Finally, \(9\notin\mathcal E\) because its binary expansion is \(1001\), completing the sharp-order statement.

## Verification
The standalone Python 3 script `verify.py` independently reconstructs the eight-state nondeterministic addition machine, performs exhaustive closure of the determinized machine with the residue and digit-parity tracker, and checks the table of all ten reachable configurations and every transition. In particular, it proves that acceptance is equivalent to residue zero for **every finite binary word**, not just for a finite numerical range. An independent numerical check enumerates eligible summands and all their sums below \(16384\). Run `python3 verify.py`; successful output ends with `VERIFY_OK`.

## Relationship to prior work
Rampersad and Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences* (arXiv:2309.04012, first submitted 2023-09-07), §7 and Theorem 20, identify this even-one-run condition as the support of their \(T_2\), a generalized Baum–Sweet-type binary sequence. They do not state an additive two-summand theorem for its support. Bell, Hare and Shallit, *When is an automatic set an additive basis?* (arXiv:1710.08353), give general decidability methods for automatic additive bases and examples involving the Cantor, evil and Rudin–Shapiro sets. Their general procedures do not, without a separate calculation, assert the exact sumset here. Chen and Wang, *On additive properties of two special sequences* (Acta Arithmetica 110 (2003), 299–303), consider parity of the **number of zero digits**, not even lengths of **one-runs**. These are distinct restrictions. The finite-state certificate above makes the exact sharp order explicit.

## Limitations
The theorem is a two-summand **existence** result, not a formula for the number of representations, nor an assertion that every positive target admits two strictly positive summands. No claim is made for the related family requiring one-run lengths divisible by an integer greater than two. General algorithms for automatic sumsets predate this application; mathematical novelty is the **specific exact equality and sharp order**, subject to possible unindexed earlier equivalent formulations. Independent scientific validation has not been performed.

## References
1. N. Rampersad and M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012 (2023), §7, Theorem 20. https://arxiv.org/abs/2309.04012
2. J. Bell, K. Hare and J. Shallit, *When is an automatic set an additive basis?*, arXiv:1710.08353 (2017), especially §§5–6. https://arxiv.org/html/1710.08353v1
3. Y.-G. Chen and B. Wang, *On additive properties of two special sequences*, Acta Arithmetica 110 (2003), 299–303, DOI: 10.4064/aa110-3-7. https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/110/3/82878/on-additive-properties-of-two-special-sequences
