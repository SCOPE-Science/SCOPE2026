# Exact cyclic three-gram reconstruction for binary words with no isolated ones

## Finding

For every integer \(n\ge1\), consider the binary circular words of length \(n\) with no cyclic occurrence of `010`. Two words are identified as necklaces precisely when one is a cyclic rotation of the other; reflection and bit complementation are **not** identifications. The observation is the ordered eight-coordinate vector \(P(w)=(N_{000},N_{001},N_{010},N_{011},N_{100},N_{101},N_{110},N_{111})\) of cyclic length-three substring multiplicities. At every position, including across the circular boundary, exactly one triple is observed. For \(n=1\) or \(n=2\), a triple is still taken using indices modulo \(n\).

**Complete realizability and reconstruction theorem.** Besides the two profiles of the constant circular words, every realizable profile is uniquely parametrized by integers \(t\ge1\), \(0\le v\le t\), \(A,B\ge0\), with \(A=0\) whenever \(v=0\), via

\[
P=(A,v,0,t,v,t-v,t,B),\qquad n=3t+v+A+B.
\]

Define \(F(t,v,A,B)\) to be the number of necklaces realizing that profile. For \(v>0\), its **exact** value is

\[
F(t,v,A,B)=\frac1t\sum_{d\mid\gcd(t,v,A,B)}\!\varphi(d)
{t/d\choose v/d}{A/d+v/d-1\choose v/d-1}
{B/d+t/d-1\choose t/d-1}.
\]

For \(v=0\), necessarily \(A=0\), and the value is

\[
F(t,0,0,B)=\frac1t\sum_{d\mid\gcd(t,B)}\varphi(d)
{B/d+t/d-1\choose t/d-1}.
\]

The two constant profiles each have one realization. Here \(\varphi\) is Euler's totient and all quantities in the sums are integers; divisors are positive. These formulas give a finite, exact answer for every length and every observation.

The realizable nonconstant profile has **exactly one** necklace realization when \(t=1\), or when \(t\ge2\) and at least one of the following holds:

\[
\begin{array}{ll}
 v=0,\ A=0,\ B\le1;& v=t,\ A+B\le1;\\
 v=1,\ B=0;& v=t-1,\ A=B=0.
\end{array}
\]

These alternatives need not be disjoint; their logical union is the criterion. Every remaining realizable profile is ambiguous.

Let \(C_n\) count distinguishable profiles, and \(U_n\) count profiles with exactly one necklace realization. Their **exact ordinary generating functions** are

\[
\sum_{n\ge1}C_nz^n=
\frac{2z}{1-z}+\frac{z^3}{(1-z)(1-z^3)}+
\frac{z^4}{(1-z)^2(1-z^3)(1-z^4)},
\]

\[
\begin{aligned}
\sum_{n\ge1}U_nz^n={}&\frac{2z}{1-z}+\frac{z^3}{1-z}+\frac{z^4}{(1-z)^2}
+\frac{z^6(1+z)}{1-z^3}\\
&+\frac{z^8(1+2z)}{1-z^4}
+\frac{z^7}{(1-z)(1-z^3)}+\frac{z^{11}}{1-z^4}.
\end{aligned}
\]

Both sequences are eventually quasipolynomial with exact least quasiperiod \(12\), of degrees three and one respectively. In particular,

\[
C_n=\frac{n^3}{72}+O(n^2),\qquad
U_n=\frac{4n}{3}+O(1),\qquad
\frac{U_n}{C_n}=\frac{96}{n^2}+O(n^{-3}).
\]

The exact maximum size of a zero-error code for the stated observation channel (with arbitrary source necklaces and one deterministic full profile observed per necklace) equals \(C_n\).

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\). The forbidden pattern is the **contiguous cyclic** triple `010`, not a scattered subsequence. Overlapping cyclic occurrences count with multiplicity; indices are reduced modulo \(n\). Every admissible necklace is permitted and there is no stochastic noise, erasure, read-order information, or strand-length uncertainty. Reversal is distinguished unless it happens to equal a rotation. All counting statements concern finite integers \(n\ge1\); no asymptotic assertion is used to establish the exact formulas.

For the mixed profiles, \(t\) denotes the number of runs of ones, \(v\) counts zero runs of length at least two, \(A\) counts excess zeros beyond the first two in those runs, and \(B\) counts excess ones beyond the first two in each one run. These quantities are recovered directly from distinct coordinates of \(P\), so the parameterization has no overcounting of profiles.

## Proof

**1. Run decomposition.** An admissible mixed circular word has both letters. Every one-run has length at least two: a singleton one between zeros would create the forbidden `010`. Every zero-run has length at least one. Choose the beginning of a one-run as a temporary origin and write

\[
w=1^{2+b_1}0^{c_1}\cdots1^{2+b_t}0^{c_t},
\qquad b_i\ge0,\quad c_i\ge1.
\]

Two such run-pair descriptions define the same necklace exactly when their \(t\) pairs are cyclic rotations. Indeed, every origin at a one-run boundary is obtained this way, and no other origin preserves the chosen run-boundary convention.

For each one-run, exactly one occurrence of `011` and one of `110` straddle its two boundaries; its internal triples include exactly \(b_i\) occurrences of `111`. A zero-run of length one contributes one `101`. A zero-run of length at least two contributes one each of `100` and `001`, plus \(c_i-2\) occurrences of `000`. There are no `010` triples. Let \(v=|\{i:c_i\ge2\}|\), \(A=\sum_{i:c_i\ge2}(c_i-2)\), and \(B=\sum_i b_i\). Then the profile has the displayed form and its coordinate sum is \(n=3t+v+A+B\). If \(v=0\), necessarily \(A=0\).

Conversely, for any admissible parameter quadruple, choose \(v\) of the \(t\) zero-runs long, assign \(A\) nonnegative extra zeros among them, and assign \(B\) nonnegative extra ones among the \(t\) one-runs. This constructs the desired circular word. No such construction collapses to a constant word. The all-zero and all-one necklaces contribute the other two profiles, distinct from every mixed profile and each other.

**2. Fiber enumeration.** Regard the \(t\) one-run/zero-run pairs as labeled slots temporarily. A slot carries a nonnegative one-run extra, and its zero-run is either short (length one) or long (length two plus a nonnegative extra). If \(v>0\), the number of labeled configurations is

\[
{t\choose v}{A+v-1\choose v-1}{B+t-1\choose t-1}.
\]

A rotation of the slots whose cyclic subgroup has order \(d\) fixes a configuration precisely when the configuration is a \(d\)-fold repetition. Thus \(d\) divides \(t,v,A,B\). On the \(t/d\) basic slots the number of choices is the corresponding product of binomial coefficients with all four parameters divided by \(d\). There are \(\varphi(d)\) cyclic rotations of order \(d\). Burnside's lemma divides their sum by \(t\), giving \(F\) for \(v>0\). If \(v=0\), there are no long zeros and \(A=0\); only the distribution of \(B\) among \(t\) slots remains, giving the other formula. This argument also proves that all fiber counts are integers and that repeated-period necklaces are counted correctly.

**3. All and only singleton fibers.** For \(t=1\), there is only one run pair, so every feasible parameter choice produces one necklace. Assume \(t\ge2\).

If \(v=0\), only \(B\) is distributed over \(t\) cyclic slots. Totals zero and one each have one orbit. For \(B\ge2\), the distributions \((B,0,\ldots,0)\) and \((B-1,1,0,\ldots,0)\) have different multisets and hence yield different orbits.

If \(v=t\), all zero gaps are long and there are two distinguishable extra compositions of totals \(A\) and \(B\). When \(A+B\le1\) one orbit results. If either total exceeds one, concentrating it in one slot versus splitting it into two slots gives different orbits. If \(A=B=1\), placing the two extras in the same slot versus in different slots gives different orbits.

Now \(0<v<t\). If \(v=1\), the unique long zero gap anchors the cyclic slots; \(A\) is forced onto it. With \(B=0\) there is one orbit; with \(B>0\), placing all \(B\) extras on two different one-run positions relative to that anchor gives distinct orbits. If \(v=t-1\) and \(t\ge3\), the unique short gap anchors all positions. When \(A=B=0\) there is one orbit. If \(A>0\), two distinct long-gap locations are available for all \(A\) extras; if \(B>0\), two distinct one-run locations are available. These choices give different orbits.

Finally, when \(1<v<t-1\), the cyclic pattern of long and short gaps can already be chosen with all long gaps adjacent or with two separated blocks; these patterns have different numbers of blocks and are not rotations. Assigning any extras to allowed positions cannot erase this difference. The cases exhaust the possibilities, including the overlap \(v=t-1=1\) at \(t=2\), proving the criterion.

**4. Distinct-profile generating function.** For every \(t\ge1\), the case \(v=0\) has \(A=0\) and unrestricted \(B\), contributing \(z^{3t}/(1-z)\). For each \(1\le v\le t\), independent nonnegative \(A,B\) contribute \(z^{3t+v}/(1-z)^2\). Sum first over \(t\), then over \(v\), noting \(t\ge v\):

\[
\sum_{t\ge1}\frac{z^{3t}}{1-z}=\frac{z^3}{(1-z)(1-z^3)},\qquad
\sum_{v\ge1}\sum_{t\ge v}\frac{z^{3t+v}}{(1-z)^2}
=\frac{z^4}{(1-z)^2(1-z^3)(1-z^4)}.
\]

Adding the constant-word contribution \(2z/(1-z)\) proves the formula for \(C_n\).

**5. Unique-profile generating function.** The \(t=1\) cases contribute \(z^3/(1-z)+z^4/(1-z)^2\). For each \(t\ge2\), the four singleton alternatives, partitioned without duplication by \(v=0\), \(v=t\), \(v=1\), and \(v=t-1\) with the last restricted to \(t\ge3\), contribute respectively

\[
\frac{z^6(1+z)}{1-z^3},\quad
\frac{z^8(1+2z)}{1-z^4},\quad
\frac{z^7}{(1-z)(1-z^3)},\quad
\frac{z^{11}}{1-z^4}.
\]

The constant profiles contribute \(2z/(1-z)\). This proves the formula for \(U_n\).

**6. Asymptotics and exact quasiperiod.** Only the third-order excess denominator factor of the mixed-profile generating function produces a pole of order four at \(z=1\). Its leading singular term is \(1/[12(1-z)^4]\); coefficient extraction gives \(C_n=n^3/72+O(n^2)\). The singleton generating function has a double pole at \(z=1\) with leading coefficient \(1+1/3=4/3\), so \(U_n=4n/3+O(1)\). Division gives the unique-profile fraction.

All poles are roots of unity of orders dividing \(12\), hence the coefficients are eventually quasipolynomial with period dividing \(12\). The profile function has noncanceled poles at primitive third and fourth roots (at a cube root \(\omega\ne1\), the reduced numerator in the \((1-z^3)\)-part is \(1-\omega+\omega^2=-2\omega\ne0\)); its \((1-z^4)\)-term is nonzero at primitive fourth roots. For the singleton function, the \((1-z^3)\)-terms have numerator \(1+z-z^2\) at primitive third roots and the \((1-z^4)\)-terms have numerator \(1+2z+z^3\) at primitive fourth roots, neither vanishing. Thus both eventual quasiperiods are exactly \(12\).

**7. Zero-error coding interpretation.** Words with different profiles are distinguishable, while two necklaces with the same profile are indistinguishable under this deterministic observation. A zero-error code can select at most one representative per profile, and choosing one representative for every profile attains \(C_n\). This is a finite pigeonhole argument, independent of how efficiently the representatives are encoded.

## Verification

Run `python3 verify.py` from the directory containing this file. The program uses only Python standard-library exact arithmetic. It independently enumerates every indexed binary circular word through length \(18\), groups them into actual rotational necklaces and actual cyclic triple profiles, and compares every profile's fiber size with the Burnside formula. It compares generating-function coefficients through length \(150\), checks the full singleton criterion across a separate finite parameter box, and reports `VERIFY_OK` on success. Actual execution produced `VERIFY_OK literal_indexed_words=524286 literal_n=1..18 matched_profiles=522 generating_functions_n=1..150 singleton_cases_checked=12312`. These finite checks corroborate but are not substitutes for the infinite arguments above.

## Relationship to prior work

Kiah, Puleo and Milenkovic developed sequence-profile coding and restricted de Bruijn graph methods, including polynomial-order and quasipolynomial bounds for constrained profile enumeration. The theorem here fixes one particular forbidden cyclic triple and determines **every finite profile and every rotational fiber**, including the singleton spectrum; the cited general bounds do not state these formulas. Chee and collaborators analyze maximum-length, distinct-window run-length-limited sequences; their counting problem is different from full multiplicity profiles and rotational reconstruction. The method of Jacquet, Knessl and Szpankowski enumerates classical first-order Markov types, rather than this restricted second-order type with explicit fibers. Recent work on reconstruction from substring **compositions** considers observations that erase letter order inside a substring and is not the full ordered cyclic three-gram channel defined here.

## Limitations

This result applies only to the exact cyclic binary full-three-gram multiplicity observation with the factor `010` forbidden. It does not cover noisy or incomplete reads, reversal identification, mixed strand collections, longer read lengths, or other forbidden factors. Exact completeness and originality relative to every possible presentation in older constrained Markov-type literature have not been independently audited. The finite verifier is not a proof of the all-length statements, which instead follow from run decomposition, Burnside enumeration and rational generating functions.

## References

1. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, first publicly posted 2024-03-03. https://arxiv.org/abs/2403.01454
2. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, first publicly posted 2015-02-02. https://arxiv.org/abs/1502.00517
3. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings, 2010, DOI:10.46298/dmtcs.2768. https://dmtcs.episciences.org/2768
4. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, posted 2022-08-31. https://arxiv.org/abs/2208.14963
