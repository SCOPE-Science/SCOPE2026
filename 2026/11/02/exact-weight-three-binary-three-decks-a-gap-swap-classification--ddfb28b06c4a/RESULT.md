# Exact weight-three binary three-decks: a gap-swap classification and generating function

## Finding

Let \(D_{3,3}(n)\) be the number of distinct length-three scattered-subsequence decks among binary words of length \(n\) with exactly three ones. The exact identity is

\[
\sum_{n\ge0}D_{3,3}(n)z^n
=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

This proves the generating-function prediction stated as Conjecture 1 of Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao [2]. More strongly, every fiber of the three-deck map on weight-three words consists of either a singleton or exactly one explicit gap-swapped pair. The first nonsingleton fiber is at length seven: `1000110` and `0110001`.

## Assumptions and scope

All words are **linear**, binary, and indexed from zero. For any binary word \(w\) and any three-bit pattern \(v\in\{0,1\}^3\), let \(\binom{w}{v}\) be the number of increasing triples of positions that spell \(v\). The complete three-deck \(\mathcal D_3(w)\) is the vector of these eight integer multiplicities. We compare only length-\(n\) words having exactly three ones. For \(n<3\), define \(D_{3,3}(n)=0\).

Write the three one-positions of a word as \(0\le p<q<r<n\), and its positive consecutive position-gaps as \(a=q-p\), \(b=r-q\). Then a distinct three-deck-equivalent word exists if and only if \(a\ne b\), \(3\mid(a-b)\), and the triple

\[
(p',q',r')=\left(p+\frac{a-b}{3},\ p+\frac{a-b}{3}+b,\ p+\frac{a-b}{3}+a+b\right)
\]

has all entries between \(0\) and \(n-1\). If it exists, it is the only distinct equivalent word, and applying the operation again returns the original. Let \(U(n)\) count unordered colliding pairs. Then

\[
U(n)=\sum_{h\ge1}\sum_{b\ge1}\max\{0,n-2b-4h\},\qquad
D_{3,3}(n)=\binom n3-U(n).
\]

Every three-deck equivalence class therefore has at most two members. The maximum size of a code distinguishing all its weight-three codewords by their three-decks is \(D_{3,3}(n)\), achieved by choosing one word from each class.

## Proof

**Step 1: The three-deck is equivalent to three positional statistics.** Set

\[
L=2p+q,\qquad T=r-p,\qquad Q=p^2+q^2+r^2.
\]

Directly counting scattered patterns with two ones gives

\[
\binom w{011}=L-1,\qquad
\binom w{101}=2T-4,\qquad
\binom w{110}=3n-4-L-2T.
\]

Let \(N=n-3\) be the number of zeros, and put \(c_1=p\), \(c_2=q-1\), \(c_3=r-2\). These are the numbers of zeros preceding each successive one. Their first two power sums satisfy

\[
B:=\sum_{i=1}^3c_i=L+T-3,\qquad
S:=\sum_{i=1}^3c_i^2=Q-2L-4T+5.
\]

Consequently, the patterns with one one satisfy

\[
\binom w{001}=\frac{S-B}{2},\qquad
\binom w{010}=NB-S,\qquad
\binom w{100}=\frac{3N(N-1)-(2N-1)B+S}{2}.
\]

Finally \(\binom w{111}=1\) and \(\binom w{000}=\binom N3\). Thus every coordinate of the three-deck is determined by \((n,L,T,Q)\). Conversely its coordinates for `011`, `101` and `001` recover them: \(L=\binom w{011}+1\), \(T=(\binom w{101}+4)/2\), and \(Q=2\binom w{001}+3L+5T-8\). Hence, for fixed \(n\), two weight-three words have the same three-deck **if and only if** their \((L,T,Q)\) triples agree.

**Step 2: Classify all possible mates.** Fix \(L,T\) and express \(q=L-2p\) and \(r=p+T\). Their squared-position sum becomes

\[
Q=6p^2+(2T-4L)p+L^2+T^2.
\]

For any specified \((L,T,Q)\), this quadratic has at most two values of \(p\). If one is \(p\), the other, counted with multiplicity, is \(p'=(2L-T)/3-p=p+(a-b)/3\). The corresponding positions are \(q'=p'+b\) and \(r'=p'+a+b\). Since \(a,b\ge1\), their strict order is automatic; they form a valid distinct second word exactly under the stated divisibility, inequality and endpoint conditions. Swapping \(a\) and \(b\) again negates the positional displacement, proving that all nonsingleton classes are pairs and that no larger classes exist.

**Step 3: Count each pair exactly once.** Orient every nonsingleton pair so its first representative has \(a>b\). The divisibility criterion is equivalent to \(a=b+3h\) with integers \(h\ge1\), \(b\ge1\). If its initial one occurs at \(p\ge0\), its mate begins at \(p+h\), has gaps \(b\) and \(b+3h\), and ends at \(p+2b+4h\). Validity of both representatives is therefore equivalent to

\[
0\le p\le n-1-(2b+4h).
\]

For each \((b,h)\) there are \(\max\{0,n-2b-4h\}\) choices of \(p\). Every colliding pair is counted once, so summing yields \(U(n)\) as claimed. The total number of weight-three words is \(\binom n3\); subtracting one for each nonsingleton fiber gives the exact number of distinct decks.

**Step 4: Generate the counts.** For fixed \(b,h\), summing the number of admissible \(p\) over lengths gives

\[
\sum_{n\ge0}\max\{0,n-2b-4h\}z^n
=\frac{z^{2b+4h+1}}{(1-z)^2}.
\]

Summing the geometric series for \(b,h\ge1\),

\[
\sum_{n\ge0}U(n)z^n
=\frac{z}{(1-z)^2}\frac{z^2}{1-z^2}\frac{z^4}{1-z^4}
=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

Since \(\sum_{n\ge0}\binom n3z^n=z^3/(1-z)^4\), subtracting proves the displayed generating function for every \(n\ge0\). The denominator of the collision term behaves as \(8(1-z)^4\) at \(z=1\), so \(U(n)=n^3/48+O(n^2)\) and \(D_{3,3}(n)=7n^3/48+O(n^2)\). All identities are exact formal power-series identities, not analytic approximations.

## Verification

The standalone standard-library checker `verify.py` reconstructs each three-deck via two independent methods: literal enumeration of all increasing index triples (for \(3\le n\le15\)), and a length-three subsequence dynamic program. For every \(3\le n\le22\), it enumerates every \(\binom n3\) word, compares fibers built from literal decks with fibers built from \((L,T,Q)\), checks every predicted partner in both directions, establishes that no fiber exceeds size two, and independently evaluates the double-sum and generating-function coefficient. Running `python3 verify.py` completes with `VERIFY_OK`. The finite checks corroborate, but do not replace, the all-length algebraic and combinatorial proof above.

For illustration, at lengths \(n=6,7,8,9,10,12,15,20,22\), the respective counts \(D_{3,3}(n)\) are \(20,34,54,80,114,206,420,1040,1400\). At length seven the sole collision is the pair of one-position triples \((0,4,5)\) and \((1,2,6)\).

## Relationship to prior work

Rigo and Salimov [1], publicly available from 27 May 2013, introduced the general framework of binomial equivalence of words and studied complexity for factors of infinite words, not the present fixed-weight complete-deck enumeration. Chrisnata and collaborators [2] investigated exact deck counts and the fixed-weight subproblem. Their section 5.3 proves \(D_{3,3}(n)=\Theta(n^3)\), displays the same generating function as **Conjecture 1**, and numerically verifies its initial twenty coefficients; it does not prove that formula or classify all fibers. The present algebraic gap-swap argument supplies those missing implications. The later general-alphabet work of Nilforoushan and Parvaresh [3] studies the overall number of decks and its growth exponent; its public abstract does not establish this fixed-weight exact distribution. Full-text historical priority beyond the inspected sources remains a risk.

## Limitations

The result is restricted to binary **linear** words of Hamming weight exactly three, and a complete noiseless three-subsequence deck. It does not classify other weights, arbitrary-alphabet words, contiguous-substring observations, circular rotations, corrupted decks, or efficient decoding in an arbitrary error model. The proof establishes an all-length counting identity and an explicit two-element-fiber classification; the finite verifier is only a corroborating calculation. Historical originality is based on the inspected literature and search comparisons, not an exhaustive proof of priority.

## References

[1] M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228. Public author text available 27 May 2013. https://orbi.uliege.be/handle/2268/149313

[2] J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the number of distinct k-decks: Enumeration and bounds*, Advances in Mathematics of Communications 17 (2023), 960–978; online 30 August 2021. Section 5.3, Conjecture 1. https://doi.org/10.3934/amc.2021032 ; author full text https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf

[3] A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (2026). https://arxiv.org/abs/2609.23106
