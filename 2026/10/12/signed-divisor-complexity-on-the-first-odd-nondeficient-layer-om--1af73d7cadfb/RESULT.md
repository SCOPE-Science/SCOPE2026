# Signed-divisor complexity on the first odd nondeficient multiplicity layer
## Finding
For an odd positive integer \(n\), let \(\Omega(n)\) count prime factors with multiplicity and let \(\sigma(n)\) be the divisor-sum function. Assume \(\Omega(n)=5\) and \(\sigma(n)\ge 2n\). For a \(\{-1,1\}\)-perfect presentation
\[
n=1+\sum_{1<d<n,\,d\mid n}\lambda_d d,\qquad \lambda_d\in\{-1,1\},
\]
define \(\nu_-(n)\) to be the minimum number of negative coefficients among all such presentations.

The exact spectrum is
\[
\#\{n:\nu_-(n)=1\}=17,\quad
\#\{n:\nu_-(n)=2\}=1,\quad
\#\{n:\nu_-(n)=3\}=88,
\]
\[
\#\{n:\nu_-(n)=4\}=0,\qquad
\#\{n:\nu_-(n)=5\}=15.
\]
The unique case with \(\nu_-(n)=2\) is \(n=2205\). The sharp cases with \(\nu_-(n)=5\) are
\[
19635,26565,82005,84315,95865,116655,118965,151305,172095,181335,199815,206745,222915,262185,296835.
\]
Thus every odd nondeficient integer with \(\Omega(n)=5\) is \(\{-1,1\}\)-perfect, and five negative coefficients always suffice; the constant five is sharp.

## Assumptions and scope
The condition \(\sigma(n)\ge2n\) is called nondeficiency in standard terminology. Ross used the word abundant for this weak inequality. The theorem is only about odd integers with total prime-factor multiplicity exactly five; it makes no assertion for larger \(\Omega\).

Because \(\Omega(n)=5\) is odd, such an odd \(n\) is not a square. Hence \(\sigma(n)\) is even. Put
\[
H(n)=\frac{\sigma(n)-2n}{2}.
\]
For the numbers under consideration, \(H(n)\) is a nonnegative integer.

## Proof
Start with all nontrivial proper divisors carrying coefficient \(+1\). Their contribution together with the fixed initial \(+1\) is \(\sigma(n)-n=n+2H(n)\). Flipping the signs on a subset \(T\) of nontrivial proper divisors subtracts \(2\sum_{d\in T}d\). Therefore
\[
\nu_-(n)=\min\left\{|T|:\ T\subseteq\{d:1<d<n,\ d\mid n\},\ \sum_{d\in T}d=H(n)\right\}.
\]
This is the cardinality-refined form of the standard subset-sum criterion.

It remains to make the \(\Omega(n)=5\) nondeficient layer finite without an arbitrary size cutoff. If \(I(n)=\sigma(n)/n\), then \(I(p^a)<p/(p-1)\). Support of size one or two is impossible, since even the two smallest odd primes give \((3/2)(5/4)<2\).

For three-prime support, the same Euler-factor bound forces the two smallest primes to be \(3\) and \(5\): replacing them by \(5,7\), or replacing the second by \(7\), already makes the maximal three-support Euler product less than \(2\). The exponent partitions are \((3,1,1)\) and \((2,2,1)\). The marginal multiplier \(I(p^{a+1})/I(p^a)=1+(p-1)/(p(p^{a+1}-1))\) decreases with \(p\), so assigning larger exponents to smaller primes maximizes abundancy. Thus a third prime \(q\) must satisfy respectively
\[
I(3^3)I(5)I(q)=\frac{16}{9}\frac{q+1}{q}\ge2
\]
or
\[
I(3^2)I(5^2)I(q)=\frac{403}{225}\frac{q+1}{q}\ge2,
\]
forcing \(q=7\). All exponent placements on \(3,5,7\) can therefore be checked exactly.

For four-prime support the exponent pattern is \((2,1,1,1)\). Exact extremal products force the two smallest primes to be \(3,5\). If \(q\) is the largest prime, moving the square to \(3\) and the third prime down to \(7\) only increases \(I(n)\), so
\[
2\le I(n)\le I(3^2)I(5)I(7)I(q)=\frac{208}{105}\frac{q+1}{q},
\]
which gives \(q\le104\), hence \(q\le103\) for prime \(q\).

For five-prime support, squarefreeness is forced by \(\Omega(n)=5\). The first three primes must be \(3,5,7\): the extremal products on \(5,7,11,13,17\), on \(3,7,11,13,17\), and on \(3,5,11,13,17\) are all below \(2\). If \(q\) is the largest prime, then
\[
2\le I(n)\le I(3)I(5)I(7)I(11)I(q)=\frac{768}{385}\frac{q+1}{q},
\]
so \(q\le384\), hence \(q\le383\).

These symbolic bounds reduce the theorem to a finite exact set with no search cutoff: the packaged verifier enumerates every admissible prime/exponent pattern and obtains exactly \(121\) nondeficient integers, from \(945\) to \(442365\). For each one, it computes \(H(n)\), enumerates subsets of nontrivial proper divisors in increasing cardinality through five, and records the first successful cardinality. The resulting counts are exactly \(17,1,88,0,15\). For every claimed value \(k\), the certificate file records a size-\(k\) witness and the verifier exhaustively rejects every smaller cardinality.

## Verification
Run `python3 verify.py` beside `spectrum.csv`. The checker uses only the Python standard library. It rederives the finite support bounds, regenerates the full \(121\)-integer boundary layer, checks the divisor-sum inequality and \(\Omega(n)=5\), recomputes every \(H(n)\), verifies every stored witness, and exhaustively rejects all smaller-cardinality subsets. Its expected terminal line is:

`VERIFY_OK boundary=121 spectrum=17,1,88,0,15 max_negative=5 extremals=15`

The computation is exhaustive only after the symbolic prime bounds above; it is not being used as evidence for an unbounded search.

## Relationship to prior work
Ross introduced \(\mathcal S\)-perfect numbers and conjectured that every nonsquare odd nondeficient integer is \(\{-1,1\}\)-perfect. His paper reports the odd nondeficient cases below \(10^4\) as positive examples but does not define or classify the minimum number of negative signs in a presentation.

Campbell later gave the exact subset-sum equivalence \(H(n)=\sum_{d\in T}d\) and constructed infinite counterexample families to Ross's conjecture. That criterion motivates \(\nu_-(n)\), but Campbell does not study its minimum cardinality on the \(\Omega=5\) layer.

A later certified finite-window study proves that every odd nonsquare nondeficient integer up to \(10^6\) has a presentation with at most seven negative coefficients. Since every integer classified here is at most \(442365\), that result already covers existence and the coarse bound seven. It does not imply the exact spectrum \(\{1,2,3,5\}\), the absence of four, the sharp bound five, or the fifteen sharp cases proved here.

## Limitations
This is a finite but natural boundary classification. It does not claim that five negative coefficients suffice for all odd nondeficient integers, nor does it contradict the known failure of Ross's unrestricted conjecture. The originality comparison is limited by the possibility of unindexed computations or private tables containing the same \(\Omega=5\) spectrum.

## References
1. T. Ross, “A Perfect Number Generalization and Some Euclid-Euler Type Results,” *Journal of Integer Sequences* 27 (2024), Article 24.7.5; published September 8, 2024. Primary MSC 11A25. https://cs.uwaterloo.ca/journals/JIS/VOL27/Ross/ross3.html
2. J. M. Campbell, “Disproofs of two conjectures concerning nondeficient numbers,” arXiv:2607.11043 (2026); later *Canadian Mathematical Bulletin*. In particular, Lemma 2.1 gives the subset-sum criterion used here.
3. “\(\{-1,1\}\)-perfect numbers: a certified window to \(10^6\), seven negative signs, and the least counterexample to Ross's Conjecture 17,” public research record, 2026. The relevant comparison is the bound of seven negative coefficients through \(10^6\).
