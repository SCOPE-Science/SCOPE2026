# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  Leonetti's 2026 theorem identifies every sufficiently large even nice number with a double \(2p\) where \(p\) is prime and \(p-1\) is squarefree, while the 2018 odd theorem identifies odd nice numbers with safe primes.  The latter contribute \(O(X/(\log X)^2)\) by the standard two-dimensional upper sieve and therefore cannot affect the main \(X/\log X\) term.

For the even branch, the Möbius identity for the squarefree indicator reduces each fixed progression to compatible prime progressions modulo \(\operatorname{lcm}(M,d^2)\).  A polylogarithmic truncation is covered by Siegel--Walfisz; the complementary \(d\)-range is bounded by \(O(Y/D+\sqrt Y)\).  The resulting absolutely convergent constant factors prime-by-prime.  The three local cases \(q\nmid M\), \(q\parallel M\), and \(q^2\mid M\) reproduce exactly the stated Euler product and the zero obstructions.  Small exceptional primes and small nice numbers affect only \(O(1)\).

The global specialization gives Artin's constant, and the modulo-6 specialization gives constants \(2\mathfrak A/5\) and \(3\mathfrak A/5\), summing to \(\mathfrak A\).  The finite verification artifact independently agrees with both the Artin-density scale and the predicted \(2/5\)--\(3/5\) local split.

## Originality

**PASS, to the best of our knowledge.**  The motivating 2026 preprint was inspected through its theorem and proof text.  It completes the even structural classification but does not state a counting asymptotic, residue-class law, Artin-constant consequence, or local-bias formula.  The 2018 odd classification is explicitly restated there.  Searches using the permutation-power definition, "nice numbers", squarefree shifted primes, Artin's constant, asymptotic counting, residue classes, and arithmetic progressions did not locate the fixed-modulus theorem stated here.

The analytic facts themselves are not claimed as new.  Mirsky's classical work gives the Artin-constant density of primes with squarefree predecessor, and Bienvenu studies substantially stronger linear patterns in this dense subset of the primes.  Those results establish that the squarefree-prime distribution is prior art; the contribution reviewed here is the explicit fixed-modulus law for the newly completed class of nice numbers, together with the proof that the unresolved safe-prime branch is lower order and the derivation of its local constants.

The most relevant source not fully inspected was Kowitz, *Generalized “Riesel” numbers and nice numbers* (DOI 10.1142/S1793830924501040).  Available bibliographic and abstract material describes generalized Riesel numbers and the counterexample \(62\) to Leonetti's earlier conjecture, not asymptotic counting.  Its full text could in principle contain an unadvertised distribution observation, so it remains a residual originality risk.  Mirsky's 1949 original article was also not inspected in full; later sources clearly attribute the shifted-squarefree-prime density to it, so this is a coverage risk only for the analytic ingredient, not evidence of an earlier theorem about Leonetti nice numbers.

## Value

**PASS.**  The result turns a pointwise classification into a complete asymptotic distribution theorem.  It shows unconditionally that nice numbers have order \(X/\log X\) with leading constant \(\mathfrak A/2\), despite the open infinitude problem for the odd safe-prime branch, and it determines the limiting mass in every fixed residue class.  The explicit local factors expose genuine arithmetic bias, already visible in the \(2/5\)--\(3/5\) split modulo \(6\).

## Limitations

The theorem is for fixed moduli only.  It does not provide uniformity when \(m\) grows with \(X\), optimize an error term, or prove any new result on the infinitude or asymptotic density of Sophie Germain primes.  It also does not claim novelty for the classical shifted-squarefree-prime sieve.
