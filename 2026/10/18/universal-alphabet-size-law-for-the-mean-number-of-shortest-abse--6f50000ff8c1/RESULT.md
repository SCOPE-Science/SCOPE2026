# Universal alphabet-size law for the mean number of shortest absent subsequences

## Finding

Fix a labeled alphabet \(\Sigma\) of cardinality \(q\ge3\). For a word \(w\in\Sigma^n\), let \(\iota_\Sigma(w)\) be the largest \(k\ge0\) for which every word in \(\Sigma^k\) occurs as a scattered subsequence of \(w\); let \(s_\Sigma(w)\) be the number of absent words of length \(\iota_\Sigma(w)+1\). Set
\[
A_q(n)=\sum_{w\in\Sigma^n}s_\Sigma(w),\qquad F_q(z)=\sum_{n\ge0}A_q(n)z^n.
\]
The empty word is included at \(n=0\), and the ambient alphabet is fixed even if \(w\) omits some letters.

For each integer \(m\ge0\), define the rational series
\[
G_m(z)=\sum_{j=0}^{m}\frac{(-1)^j\binom{m}{j}}{1-(m-j)z},
\]
\[
H_m(z)=z\sum_{j=0}^{m}(-1)^j\binom{m}{j}
\left(\frac1{1-(m-j+1)z}-\frac1{1-(m-j)z}\right)
\frac1{1-(m-j+1)z}.
\]
In particular, \(G_0(z)=1\). Set
\[
D_q(z)=zG_{q-1}(z)+(q-1)z^2\bigl(G_{q-2}(z)+zG'_{q-2}(z)\bigr),
\]
\[
E_q(z)=zG_{q-1}(z)+(q-2)zH_{q-3}(z).
\]
Then the **exact all-length, all-alphabet-size law** is
\[
\boxed{F_q(z)=\frac{q}{\bigl(1-(q-1)z\bigr)\bigl(1-D_q(z)-(q-1)E_q(z)\bigr)}}\qquad(q\ge3).
\]
Thus \(\mathbb E[s_\Sigma(W_n)]=A_q(n)/q^n\) when \(W_n\) is uniform on \(\Sigma^n\). Every \(F_q\) is rational, so the entire mean sequence obeys a fixed constant-coefficient recurrence for each fixed alphabet size.

For the first nonbinary alphabet,
\[
\boxed{F_3(z)=\frac{3(1-z)^2}{1-4z+5z^2-14z^3+20z^4-4z^5}}.
\]
Its initial coefficients are \(3,6,12,60,204,576,1908,6456,20508,\ldots\). If \(\rho\) denotes the smallest positive root of the displayed denominator, then
\[
\rho=0.308787976762659\ldots,\qquad
\mathbb E[s_\Sigma(W_n)]\sim
1.692088487\ldots\,(1.079489353\ldots)^n
\quad(q=3).
\]
The asymptotic is for \(n\to\infty\) with a fixed three-letter alphabet.

## Assumptions and scope

All generating functions are formal power series in \(z\) with integer coefficients before the asymptotic specialization. The alphabet is labeled, and an absent subsequence is an order-preserving pattern whose embedding positions need not be adjacent. The definition of universality here is relative to the **fixed** full alphabet \(\Sigma\), not the possibly smaller set of letters occurring in a particular word. Consequently a word that does not use every letter has index zero and its shortest absent subsequences are precisely its missing letters. The theorem applies to every integer \(n\ge0\) and \(q\ge3\) without assumptions on letter frequencies.

## Proof

**1. Greedy full-alphabet arches.** Cut \(w\) greedily into the shortest consecutive prefixes that contain every letter of \(\Sigma\), then repeat with the unconsumed suffix. This gives a unique factorization
\[
w=a_1a_2\cdots a_Kr,
\]
where each complete arch \(a_i\) contains all \(q\) letters, its last letter occurs nowhere earlier in that arch, and the rest \(r\) omits at least one letter. Every length-\(K\) pattern can be embedded by selecting its \(i\)-th letter from arch \(a_i\). Conversely, choose the last letters of the arches and then a letter absent from \(r\); greedily matching that length-\(K+1\) pattern uses one last letter per arch and fails in \(r\). Thus \(K=\iota_\Sigma(w)\), including the case \(K=0\).

**2. Exact absent-pattern criterion.** Fix any target \(u=u_1\cdots u_{K+1}\). Scan \(w\) from left to right, greedily matching each next target symbol. If \(u\) is absent, at least one target symbol is still unmatched whenever an arch begins. Since that arch contains every letter, it matches at least one target symbol. There are \(K\) arches but only \(K\) matches in total if the target is absent: no pattern of length \(K\) can remain unmatched by step 1. Hence **an absent target is characterized exactly by one greedy match in each arch and no greedy match in \(r\)**. The converse follows immediately because only \(K\) target symbols then match.

**3. Complete-arch transition series.** Fix successive target symbols \(x,y\in\Sigma\). Let \(T_{xy}(z)\) count complete arches on which the greedy target scan matches \(x\) exactly once and has no subsequent opportunity to match \(y\). Every arch is uniquely \(vt\), where the terminal letter \(t\) is absent from \(v\), and \(v\) contains all of the other \(q-1\) symbols.

The series \(G_m\) counts words containing each of \(m\) prescribed symbols at least once, by inclusion–exclusion. If \(x=y\), either \(t=x\), giving \(zG_{q-1}\), or \(t\ne x\), in which case \(v\) contains exactly one \(x\), inserted in any position of a full-support word over \(q-2\) other symbols. A word of length \(\ell\) has \(\ell+1\) insertion sites. Thus
\[
T_{xx}(z)=zG_{q-1}+(q-1)z^2(G_{q-2}+zG'_{q-2})=D_q(z).
\]

If \(x\ne y\), an arch ending in \(y\) fails the condition, while one ending in \(x\) contributes \(zG_{q-1}\). For any of the remaining \(q-2\) choices of terminal letter, write \(v=pxs\), where \(p\) contains at least one \(y\) but no \(x\), and \(s\) contains no \(y\) (but may contain \(x\)). All remaining \(q-3\) symbols must occur somewhere in \(ps\). With \(r\) temporarily allowed unmarked symbols, the ordinary generating functions for \(p\) and \(s\) are respectively
\[
\frac1{1-(r+1)z}-\frac1{1-rz}
\quad\text{and}\quad \frac1{1-(r+1)z}.
\]
Multiplying, inserting the mandatory \(x\), and applying inclusion–exclusion to the \(q-3\) unmarked symbols gives exactly \(H_{q-3}\). Consequently
\[
T_{xy}(z)=zG_{q-1}+(q-2)zH_{q-3}=E_q(z)\quad(x\ne y).
\]

**4. Sum over targets and arches.** For a specified last, unmatched target letter \(y\), the rest may be any word over \(\Sigma\setminus\{y\}\), with series \(R_q(z)=1/(1-(q-1)z)\). Such a rest automatically omits at least one letter, so it is indeed a valid greedy rest. For a specified target \(u_1\cdots u_{K+1}\), its total host-word series is the product \(T_{u_1u_2}\cdots T_{u_Ku_{K+1}}R_q\). The \(q\)-by-\(q\) transition matrix has diagonal \(D_q\) and off-diagonal \(E_q\), so all row sums are \(D_q+(q-1)E_q\). Summing over every target of every admissible length, including \(K=0\), yields
\[
F_q(z)=qR_q(z)\sum_{K\ge0}\bigl(D_q(z)+(q-1)E_q(z)\bigr)^K,
\]
which is the formula claimed. The use of formal series is legitimate because every arch has length at least \(q\), so the geometric series is coefficientwise finite.

**5. Ternary simplification.** Substituting \(q=3\) into the inclusion–exclusion expressions yields
\[
D_3(z)=\frac{2z^3(3-6z+2z^2)}{(1-z)^2(1-2z)},\qquad
E_3(z)=\frac{z^3(3-4z)}{(1-z)^2(1-2z)}.
\]
Elementary cancellation gives the displayed quintic rational generating function. Its coefficients obey the corresponding order-five linear recurrence, with initial values taken from the rational numerator.

**6. Ternary asymptotic.** Write \(J_3(z)=D_3(z)+2E_3(z)\). This series has strictly nonnegative coefficients, including positive coefficients at consecutive arch lengths \(3\) and \(4\); hence its support has greatest common divisor one. On the positive real interval below \(1/2\), the function is strictly increasing, and it crosses one exactly once at \(\rho=0.308787976762659\ldots\), which is smaller than \(1/3\). Equality in the triangle inequality shows that no other complex point of modulus \(\rho\) can solve \(J_3(z)=1\): consecutive positive coefficient degrees would require \(z/|z|=1\). Its derivative is positive at \(\rho\), so the pole is simple and uniquely dominant. With \(Q(z)=1-4z+5z^2-14z^3+20z^4-4z^5\), transfer of a simple pole gives
\[
A_3(n)\sim -\frac{3(1-\rho)^2}{\rho Q'(\rho)}\rho^{-n}.
\]
Dividing by \(3^n\) gives the stated asymptotic and positive constant. This analytic argument proves an infinite-length limit; the finite checks below are only independent consistency tests.

## Verification

Run `python3 verify_qary_sas.py` with Python 3 and no third-party packages. It independently enumerates all source words up to length \(10\) for \(q=2\), through length \(8\) for \(q=3\), and through length \(6\) for \(q=4\), totaling \(17{,}349\) individual host words. It directly computes each shortest absent pattern and compares aggregated counts with independently implemented complete-arch coefficient recurrences. It also enumerates arch transitions, verifying diagonal and off-diagonal counts, and checks the ternary quintic identity through degree \(35\). The \(q=2\) checks are controls, not a novelty claim.

The formal proof of the all-length rational identity is steps 1–5. The independent checker verifies finite prefixes only and does not certify the analytic limit.

## Relationship to prior work

Kosche, Koß, Manea, and Siemer (first public preprint 2021-08-31) give the notions of shortest absent subsequences and their structural arch characterization and algorithms for individual words; their inspected Sections 2–4 do not supply an exact all-word, all-length mean for fixed alphabets of size at least three. Adamson, Fleischmann, Huch, Manea, Sarnighausen-Cahn, and Wiedenhöft (first preprint 2024-07-26) prove extremal bounds given a universality index, not an average over all words of a specified length. Manea, Ringleb, Siemer, and Winkler (2025) address output-sensitive enumeration for a supplied word, not the distribution over all words.

An exact binary first-moment law is already known and not claimed here. The new claim is explicitly restricted to \(q\ge3\): a general finite-alphabet formula and, in particular, the previously unreported ternary rational law and its asymptotic. The transition involving an additional third terminal-letter case is absent in the binary specialization. No claim of complete bibliographic uniqueness is made.

## Limitations

The theorem assumes uniform sampling across **all** labeled words of a fixed length when interpreted probabilistically; it does not give variance, concentration, conditional composition statistics, or expectations for biased or dependent sources. The asymptotic constant is reported numerically for convenience, with its exact defining equation and derivative expression supplied above. It is possible that an equivalent formula occurs in unindexed literature. The mathematical statement and checker have not undergone independent audit.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first version 2021-08-31), Sections 2–4. https://arxiv.org/abs/2108.13968
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first version 2024-07-26), Sections 2–4. https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025), Sections 1–3. https://arxiv.org/abs/2504.21471
