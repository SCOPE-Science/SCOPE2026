# The exact additive conductor for Zumkeller-plus-practical sums

## Finding
A positive integer is **Zumkeller** if its positive divisors split into two sets with equal sum; a positive integer is **practical** if each smaller positive integer is a sum of distinct positive divisors. Write \(\mathcal Z\) and \(\mathcal P\) for these sets, with \(1\in\mathcal P\).

**Theorem.** The largest positive integer outside the sumset \(\mathcal Z+\mathcal P\) is \(19067\). In particular, its exact additive conductor is \(19068\):
\[
\{n\in\mathbb Z_{>0}:n\ge19068\}\subseteq\mathcal Z+\mathcal P,
\qquad19067\notin\mathcal Z+\mathcal P.
\]
There are exactly \(720\) positive integers outside the sumset, and their complete increasing list is `exceptions.txt`.

## Assumptions and scope
All sums use **one positive Zumkeller integer and one positive practical integer**; zero is excluded from both summands. The theorem is an exact statement over all positive integers, not a density or finite-range conjecture. A finite, deterministic certificate supports the bounded part of the proof; an infinite arithmetic progression and a complete residue cover support its unbounded part.

## Proof
**1. Infinite family.** The divisors of \(945=3^3\cdot5\cdot7\) have total sum \(1920\); the subset \(\{945,3,5,7\}\) has sum \(960\), so \(945\) is Zumkeller. The coprime-multiplication lemma for Zumkeller numbers [1, Lemma 2.1] says that if \(z\in\mathcal Z\) and \(\gcd(z,u)=1\), then \(zu\in\mathcal Z\). Because \(\gcd(945,1+105t)=1\) for every nonnegative integer \(t\), we get
\[
945+99225t=945(1+105t)\in\mathcal Z\qquad(t\ge0).
\]
This improves the modulus \(945^2\) used for a qualitative existence proof in [1] to the smaller modulus \(945\operatorname{rad}(945)=99225\).

**2. Effective residue cover.** For every residue \(r\) in \(\{0,\ldots,99224\}\), let \(p_r\) be the least positive practical number congruent to \(r\) modulo \(99225\). Finite exact computation with the Stewart--Sierpiński characterization of practical numbers verifies that all \(p_r\) exist and
\[
\max_{0\le r<99225}p_r=41235272,
\]
with the maximum first occurring in residue \(56897\). To make this fully replayable, `verify_large.cpp` factors every integer through \(42000000\), constructs \(p_r\) for every residue, and checks the maximum exactly. Now, for any integer \(n\ge41236217\), choose \(r\equiv n-945\pmod{99225}\). Since \(p_r\le41235272\), there is an integer \(t\ge0\) with
\[
n=p_r+(945+99225t),
\]
which is a practical-plus-Zumkeller decomposition. No primality hypothesis on \(n\) is used.

**3. Finite interval.** The same `verify_large.cpp` enumerates all practical integers through \(42000000\), then, using the \(1989\) certified odd Zumkeller numbers in `odd_z_witnesses.txt` (all at most \(1000000\)), computes their sums with even practical integers by exact bitset convolution-by-shifts. For **every odd** \(n\) with \(19069\le n<41236217\), it obtains a representation except at \(n=20177\). That remaining case has the explicit representation \(20177=20176+1\); the verifier independently checks that \(20176\) is Zumkeller (its proper divisors contain a subset of sum \(1090\), and its full divisor sum is \(42532\)). Every even \(n\ge90\) is representable using the positive Zumkeller progressions \(18m+6\), \(18m+12\) and fixed practical summands \(6,12,20,28,40,80\). An explicit residue-by-residue construction is given in [1, Proposition 4.8], which is also immediate by checking each of the nine even residue classes modulo \(18\).

**4. Sharpness and complete exceptions.** For an odd integer, either its practical summand is \(1\) (the only odd practical number) or it is even and its Zumkeller summand is odd. But \(19066\) is not Zumkeller: it factors as \(2\cdot9533\) with divisor sum \(28602<2\cdot19066\). The exhaustive divisor-subset check for odd Zumkeller integers below \(19067\) finds exactly \(38\) candidates, and no corresponding complement \(19067-z\) is practical. Consequently \(19067\notin\mathcal Z+\mathcal P\). An independent complete finite check of every \(1\le n\le19067\) gives exactly \(720\) exceptional integers, printed in `exceptions.txt`. Combining the four steps proves the theorem.

## Verification
Run in the directory containing the three accompanying files:
```
python3 verify_small.py
g++ -O3 -std=c++17 verify_large.cpp -o verify_large
./verify_large
```
`verify_small.py` uses exact integer divisor sums and subset-sum bitsets to validate all \(1989\) odd Zumkeller witnesses, exhaust the \(38\) odd candidates below \(19067\), establish the nonrepresentation and the \(720\)-exception count, and independently check the practical-number criterion against direct divisor subset sums through \(1000\). `verify_large.cpp` independently factors all even integers through \(42000000\), checks the complete residue cover, and constructs the finite sumset certificate by machine-word bit operations. Expected output includes `SMALL_CERTIFICATE_OK` and `LARGE_CERTIFICATE_OK`.

The finite certificate is **complete** over its stated range, not an extrapolation. The global conclusion uses the proved arithmetic progression and the complete residue cover. Finite checks are not taken as a substitute for the unbounded argument.

## Relationship to prior work
Somu, Kukla and Tran [1, Proposition 4.10 in v2; Proposition 5.3 in v1] proved that \(\mathcal Z+\mathcal P\) contains all sufficiently large positive integers, but gave no explicit conductor or full list of exceptions. They also proved all even integers at least \(8\) are representable [1, Proposition 4.8], and established a separate exact maximal exception \(32761\) for **two Zumkeller summands**, which is a different sumset. Mahanta, Saikia and Yaqubi [2] investigate divisor-set structure and relationships with practical numbers, but do not give the present additive conductor. These results supply context rather than the exact bound above.

## Limitations
The proof uses a finite, reproducible exhaustive calculation over a specified interval. It is not a purely symbolic evaluation of all \(720\) exceptions, nor a classification of the number of representations. The large residue-cover bound \(41236217\) is a sufficient proof threshold; it is not claimed minimal for that method. All claims of originality are relative to the inspected references and targeted searches; prior unindexed work is possible. No independent mathematical audit is asserted.

## References
[1] S. T. Somu, A. Kukla and D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (22 October 2023), arXiv:2310.14149v2 (27 November 2023), especially Lemma 2.1, Propositions 4.8 and 4.10 in v2.

[2] P. J. Mahanta, M. P. Saikia and D. Yaqubi, *Some properties of Zumkeller numbers and \(k\)-layered numbers*, Journal of Number Theory 217 (2020), 218–236, doi:10.1016/j.jnt.2020.05.003.

[3] A. Srinivasan, *Practical numbers*, Current Science 17 (1948), 179–180; B. M. Stewart and W. Sierpiński's prime-factor characterization of practical numbers (used explicitly in both verifiers).
