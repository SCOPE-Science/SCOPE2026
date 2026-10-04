# An explicit ample number coprime to \(30\) proves the \(k=3\) case of Fink's conjecture

## Finding
Let \(a(n)\) denote the number of recursive divisors in the sense of Fink, and call \(n\) *ample* when
\[
a(n)>n.
\]

Consider
\[
N=7^{53}\cdot11^{32}\cdot13^{27}\cdot17^{20}\cdot19^{18}\cdot23^{14}\cdot29^{11}\cdot31^{11}\cdot37^{9}\cdot41^{8}\cdot43^{7}\cdot47^{7}\cdot53^{6}\cdot59^{5}\cdot61^{5}\cdot67^{5}\cdot71^{4}\cdot73^{4}\cdot79^{4}\cdot83^{4}\cdot89^{3}\cdot97^{3}\cdot101^{3}\cdot103^{3}\cdot107^{3}\cdot109^{3}\cdot113^{2}\cdot127^{2}\cdot131^{2}\cdot137^{2}.
\]
Its prime factors all exceed \(5\), so
\[
\gcd(N,30)=1.
\]
An exact ordered-factorization computation gives
\[
N=620292621350581595028788086460529920524835904967474139327792360930732793395120244743880376383226268545987559098771892559442316407609738081067885836143275657304648271565207000271510801969286511134165572223709287438361671058622276645794887113763333824201182721793334478788976256555206276595970169364248794528714439830251723041454975723539907118879778865193261927620897356292999057
\]
and
\[
a(N)=4049133544250342561183325521264172563005480191320800479542494459697603112797635044312286342288876256821977562257067011133903745199643554947861982777035319862599949177417621412966898015644050302785597441965242309323324272569620209275645157830398009101069585728309165802195604952107308511903423174568579984014507189732152001080722827137532141825789248283717033830043635021423667314688.
\]
Thus
\[
a(N)-N=4048513251628991979588296733177712033084955355415833005403166667336672380004239924067542461912493030553431574697968239241344302883235945209780914891199176586942644529146056205966626504842081016274463276393018600035885910898561586998999362943284245767245384545587372467716815975850753305626827204399215735219978475292321749357681372161808601918670368504851840568116014124067374315631>0.
\]

Therefore \(N\) is ample and is divisible by none of \(2,3,5\). This proves the \(k=3\) case of Fink's conjecture that, for every \(k\), an ample number exists that avoids the first \(k\) primes.

Fink also proves that the product of two ample numbers is ample. Consequently the powers \(N^r\), for every integer \(r\ge1\), give infinitely many ample integers coprime to \(30\).

## Assumptions and scope
Fink defines the recursive-divisor function by
\[
a(1)=1,
\qquad
a(n)=1+\sum_{d\mid n,\ d<n}a(d)
\]
for \(n>1\).

The claim is an existence result, not a minimality result. No assertion is made that the displayed \(N\) is the smallest ample number coprime to \(30\), or that the full conjecture holds for all \(k\).

The source paper gives examples avoiding the first one and first two primes and formulates the general conjecture. A 2022 follow-up conference abstract describes the general case as ongoing work and again identifies the first-two-prime example as the known computational benchmark.

## Proof
For \(n\ge2\), Fink proves that
\[
a(n)=2K(n),
\]
where \(K(n)\) is the number of ordered factorizations of \(n\) into integers greater than one.

Write
\[
n=\prod_{i=1}^r p_i^{\alpha_i}
\]
and let
\[
\Omega=\sum_{i=1}^r\alpha_i.
\]
For a fixed factorization length \(m\), distribute the \(\alpha_i\) indistinguishable copies of prime \(p_i\) among \(m\) ordered factor positions. If empty factor positions were allowed, the number of distributions would be
\[
\prod_{i=1}^r
\binom{\alpha_i+m-1}{m-1}.
\]
Inclusion-exclusion over empty factor positions therefore gives the exact number
\[
K_m(n)=
\sum_{t=1}^m
(-1)^{m-t}
\binom mt
\prod_{i=1}^r
\binom{\alpha_i+t-1}{t-1}
\]
of ordered factorizations into exactly \(m\) nonunit factors. No factorization can have more than \(\Omega\) nonunit factors, so
\[
a(n)=
2\sum_{m=1}^\Omega K_m(n).
\]

For the exponent vector
\[
(53,32,27,20,18,14,11,11,9,8,7,7,6,5,5,5,4,4,4,4,3,3,3,3,3,3,2,2,2,2)
\]
one has \(\Omega=280\). Evaluating the finite integer sum above gives exactly
\[
a(N)=4049133544250342561183325521264172563005480191320800479542494459697603112797635044312286342288876256821977562257067011133903745199643554947861982777035319862599949177417621412966898015644050302785597441965242309323324272569620209275645157830398009101069585728309165802195604952107308511903423174568579984014507189732152001080722827137532141825789248283717033830043635021423667314688.
\]
Direct multiplication of the stated prime powers gives exactly
\[
N=620292621350581595028788086460529920524835904967474139327792360930732793395120244743880376383226268545987559098771892559442316407609738081067885836143275657304648271565207000271510801969286511134165572223709287438361671058622276645794887113763333824201182721793334478788976256555206276595970169364248794528714439830251723041454975723539907118879778865193261927620897356292999057.
\]
Their difference is the positive integer
\[
4048513251628991979588296733177712033084955355415833005403166667336672380004239924067542461912493030553431574697968239241344302883235945209780914891199176586942644529146056205966626504842081016274463276393018600035885910898561586998999362943284245767245384545587372467716815975850753305626827204399215735219978475292321749357681372161808601918670368504851840568116014124067374315631.
\]
Hence \(a(N)>N\).

Because every prime factor of \(N\) is at least \(7\), the number is coprime to \(30\). This establishes the required \(k=3\) witness.

## Verification
The accompanying `verify.py` uses only exact integer arithmetic. It checks that the 30 displayed bases are distinct primes exceeding \(5\), reconstructs \(N\), computes every \(K_m(N)\) for \(1\le m\le280\) by inclusion-exclusion, reconstructs \(a(N)=2\sum_m K_m(N)\), and checks the exact values of \(N\), \(a(N)\), and \(a(N)-N\).

The verifier also checks several small signatures against the defining recursion, including prime powers and squarefree products, to catch normalization or factor-of-two errors in the ordered-factorization formula.

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Fink introduced ample numbers in 2020 and explicitly conjectured that, for every \(k\), there is an ample number avoiding the first \(k\) primes. He supplied an odd ample number and a much larger ample number avoiding \(2\) and \(3\), but no example avoiding \(2,3,5\).

Liyanage and Ranasinghe's 2022 conference contribution studies a general prime-factor template for this conjecture. Its published abstract says the work is ongoing and cites Fink's first-two-prime example as the computational state of play; it does not provide a \(k=3\) witness.

Fink's 2023 paper gives general closed expressions for the recursive-divisor function and the identity \(a(n)=2K(n)\). Those formulas make exact evaluation possible for any specified prime signature, but they do not themselves furnish an ample signature avoiding \(2,3,5\). The new content here is the explicit signature above together with its exact positive inequality.

A current open-problem index still lists Fink's conjecture as open and records no posted solution. Exact searches for an ample number avoiding \(2,3,5\), for a first-three-prime witness, and for the leading exponent pattern of the displayed number did not locate a published duplicate.

## Limitations
The result proves only the next explicit case \(k=3\); it does not settle Fink's conjecture for arbitrary \(k\).

The witness is not claimed to be minimal in size, number of prime factors, exponent sum, or any other sense. The displayed \(N\) has 30 distinct prime factors and total prime-factor multiplicity \(280\).

Search non-detection does not prove uniqueness or novelty. An unindexed or private computation could already contain another \(k=3\) witness.

## References
1. Thomas Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, first posted 24 August 2020.
2. Thomas M. A. Fink, “Number of ordered factorizations and recursive divisors,” arXiv:2307.16691v1, first posted 31 July 2023.
3. M. P. Liyanage and P. G. R. S. Ranasinghe, “An approach towards settling a conjecture on ample numbers,” *Proceedings of the 9th Ruhuna International Science & Technology Conference*, 19 January 2022, p. 41.
