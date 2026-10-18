# Independent mathematical audit

## correctness

PASS

For n-bit N with digit sum/Hamming weight w>=2, first recurrence continuation is K_{n+1}=w; subtract consecutive window sums to get K_{n+j}=2^(j-1)w-P_{j-1} for 1<=j<=n+1. Strict increasing after w and K_{2n+1}=2^n w-N>N restrict a hit to j<=n. The bounds 2^(j-1)(w-1)<N<=2^(j-1)w and 2^(n-1)<=N<2^n force j=n-ceil(log_2 w)+1 (examine boundary w=2^c). Write L=2^c,N=PL+S, 0<=S<L; the hit equation becomes 2^(n-c)w=(L+1)P+S, uniquely determining P,S by Euclidean division. The bitcount equation is necessary and sufficient, as the converse constructs n bits and verifies the hit. Weight one numbers are powers of two. Hence at most n per bit length and B2(x)<=h(h+1)/2. Independent direct complete recurrence enumeration for n=2..16 matched this construction exactly; infinite conclusion relies on algebra, not the test.

## originality

PASS

The complete published Klazar–Luca 2007 Counting Keith Numbers (PDF examined including p3 discussion) establishes a decimal density-zero bound and higher-base adaptations but explicitly exempts base 2, mentions an UNPUBLISHED Kenneth Fan construction allegedly producing all binary Keith numbers, and notes powers of two. OEIS A162363/A162724 list binary examples and recurrence shortcuts but no available public one-per-(n,w) Euclidean criterion. A potentially covering unpublished manuscript cannot be excluded; documented as material risk without treating inaccessible literature alone as failure. Best-of-knowledge O PASS.

## value

PASS

For each natural (binary bit length n,Hamming weight w) cell, the theorem gives a zero-or-one explicit exact classification via a single Euclidean division rather than a recurrence search. It yields a quadratic logarithmic counting bound and a natural rigid structure for a classic combinatorial number sequence, beyond preexisting powers-of-two and finite lists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
