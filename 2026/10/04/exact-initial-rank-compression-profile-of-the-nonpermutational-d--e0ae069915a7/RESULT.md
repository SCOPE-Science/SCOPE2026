# Exact initial rank-compression profile of the nonpermutational \(D^{\prime\prime}_n\) automata
## Finding
For the Ananichev–Gusev–Volkov automaton \(D^{\prime\prime}_n\) on \(Q=\{1,\ldots,n\}\), with \(a(i)=b(i)=i+1\) for \(1\le i\le n-2\), \(a(n-1)=a(n)=1\), \(b(n-1)=n\), and \(b(n)=2\), let \(\lambda_n(s)\) be the minimum length of a word whose image has size at most \(n-s\). For every \(n\ge4\), \(\lambda_n(1)=1\), and for every \(2\le s\le\lceil n/2\rceil\), \(\lambda_n(s)=2s-2\); for these \(s\ge2\), the unique shortest word is \((ba)^{s-1}\). Moreover, for \(s_0=\lceil n/2\rceil+1\), one has \(\lambda_n(s_0)>2s_0-2\).

Thus this classical slowly synchronizing family compresses from full rank to rank \(n-\lceil n/2\rceil\) at the fastest rate permitted by its local collision structure, but that linear pattern cannot continue to the next deficiency.

## Assumptions and scope
For \(n\ge4\), let \(Q=\{1,\ldots,n\}\). The two letters act by
\[
a(i)=b(i)=i+1\quad(1\le i\le n-2),\qquad a(n-1)=a(n)=1,
\]
\[
b(n-1)=n,\qquad b(n)=2.
\]
This is the coloring denoted \(D^{\prime\prime}_n\) in the cited Ananichev–Gusev–Volkov sources. For a word \(w\), its rank is \(|Qw|\), and \(\lambda_n(s)\) is the least \(|w|\) with \(|Qw|\le n-s\).

The statement concerns only the initial deficiency range through \(\lceil n/2\rceil\) and the strict failure of the same linear formula at the next deficiency. It does not claim a formula for the remainder of the rank profile or for the reset threshold.

## Proof
Each letter has rank \(n-1\), so one letter can decrease the current image size by at most one. The only collision of \(a\) is the pair \(\{n-1,n\}\), while the only collision of \(b\) is \(\{1,n\}\). Also \(Qa=Q\setminus\{n\}\) and \(Qb=Q\setminus\{1\}\).

After any nonempty word ending in \(a\), the image omits \(n\); after any nonempty word ending in \(b\), the image omits \(1\). Hence after the first letter the current image never contains both \(1\) and \(n\). Therefore \(b\) can decrease rank only when it is the first letter of the word.

After an effective occurrence of \(a\), the resulting image omits \(n\), so another \(a\) cannot immediately be effective. Every later effective \(a\) therefore needs at least one intervening letter, and that intervening letter must be \(b\) if equality in the length bound is to hold.

To obtain deficiency \(s\ge2\), if the first letter is \(a\), then the first drop costs one letter and each of the remaining \(s-1\) drops costs at least two letters, giving length at least \(2s-1\). If the first letter is \(b\), then the first drop is made by that \(b\), and the remaining \(s-1\) drops must be made by effective occurrences of \(a\), with a \(b\) between consecutive effective \(a\)'s. Thus every such word has length at least \(2s-2\). Equality forces the letters position by position, so the only possible equality word is
\[
(ba)^{s-1}.
\]

It remains to determine when this word actually makes every indicated drop. For \(1\le k\le\lceil n/2\rceil-1\), direct induction gives
\[
Q\setminus Q(ba)^k=\{2,4,\ldots,2k\}\cup\{n\}.
\]
Indeed, after the first \(k\) blocks the set omits \(n\) and the even states through \(2k\). Applying \(b\) shifts the surviving states from \(Q\setminus\{n\}\) one step forward, so the omitted states become \(1,3,\ldots,2k+1\). In the stated range both \(n-1\) and \(n\) are then present exactly when the next \(a\) is supposed to be effective; applying \(a\) creates the next even hole and again omits \(n\). Hence \((ba)^k\) has deficiency \(k+1\), proving \(\lambda_n(s)=2s-2\) and uniqueness for \(2\le s\le\lceil n/2\rceil\). Since either one-letter word already has rank \(n-1\), \(\lambda_n(1)=1\).

At \(k=\lceil n/2\rceil-1\), the hole pattern is saturated: for even \(n\) all even states are missing, while for odd \(n\) all even states below \(n\), together with \(n\), are missing. One further block \(ba\) does not reduce the image size. The equality argument above shows that \((ba)^{s_0-1}\) is the only word that could attain deficiency \(s_0=\lceil n/2\rceil+1\) in length \(2s_0-2\). Since it does not, \(\lambda_n(s_0)>2s_0-2\).

## Verification
The accompanying `verify.py` independently constructs the two transformations from the displayed definition. It performs exhaustive breadth-first search in the power automaton for every \(4\le n\le18\). For each \(s\le\lceil n/2\rceil\), it checks the claimed minimum length and counts shortest words, verifying that the count is one for \(s\ge2\) and that the unique word is \((ba)^{s-1}\). It also verifies that the next deficiency needs strictly more than \(2s_0-2\) letters.

Separately, direct word replay checks the explicit hole formula for every \(4\le n\le200\), and checks that one further \(ba\) block at the saturation point does not decrease rank. The archived output ends with `VERIFY_OK`.

## Relationship to prior work
Ananichev, Gusev, and Volkov introduced the family and proved that \(D^{\prime\prime}_n\) has reset threshold \(n^2-3n+2\). Their later extended treatment again presents the coloring and the same reset-threshold theorem, emphasizing that the family was extremal among then-known automata in which no letter acts as a permutation. Those results determine the final rank-one threshold, not the intermediate thresholds \(\lambda_n(s)\), the uniqueness of the short compression words, or the exact point at which the linear initial profile stops.

Targeted searches for the family name together with rank, deficiency, compression, shortest-word, and intermediate-rank terminology did not locate the statement above. General literature on word rank and subset compression supplies broader context but does not imply this family-specific profile. Search failure is not a proof of novelty; see the limitations below.

## Limitations
The proof gives only the initial half-rank profile and a strict lower bound at the next deficiency. It does not determine \(\lambda_n(s)\) beyond that boundary. The computational checks are finite corroboration, not a substitute for the symbolic proof.

The originality assessment is literature-based and cannot certify absence from every older or unindexed source. The most relevant original and extended papers were inspected at the theorem and family-definition level, and multiple searches using equivalent rank/compression terminology were run; an older equivalent statement under different terminology remains a residual bibliographic risk.

## References
1. D. S. Ananichev, V. V. Gusev, and M. V. Volkov, “Slowly synchronizing automata and digraphs,” MFCS 2010, LNCS 6281, 55–65. arXiv:1005.0129v1, first public 2010-05-02. DOI: 10.1007/978-3-642-15155-2_7.
2. D. S. Ananichev, V. V. Gusev, and M. V. Volkov, “Primitive digraphs with large exponents and slowly synchronizing automata,” Journal of Mathematical Sciences 192 (2013), 263–278. arXiv:1302.5793v2. DOI: 10.1007/s10958-013-1392-8.
