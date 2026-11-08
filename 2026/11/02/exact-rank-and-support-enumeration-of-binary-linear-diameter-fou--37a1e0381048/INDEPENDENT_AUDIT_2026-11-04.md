# Independent mathematical audit

## correctness

PASS

For an F2-linear code of Hamming diameter <=4, maximal nonzero weight <=4. RREF gives dim k<=4 via pivot-column sum; each nonzero column occurs in 2^(k-1) of all 2^k codewords, so support size s obeys s*2^(k-1)<=4(2^k-1) and s<=7. Every full-support code in this finite (s<=7,k<=4) rectangle is counted exhaustively via RREF pivot/free-column matrices and independently via full-rank multisets of k-bit nonzero columns, tested for all codeword weights, with multinomial weights divided by |GL(k,2)|. Independent complete RREF enumeration confirmed all 40 rank-support cells, totals by s = (1,1,2,6,26,91,100,30), making global B(n,k)=sum_s a(s,k) C(n,s) valid for ALL n>=0. At s=7 k<3 ruled out by weight sum, k=4 contradicted by second moments; k=3 forces all seven nonzero columns of F2^3, yielding exactly 7!/|GL(3,2)|=30 labeled simplex copies. Finite coefficient computation is exhaustive because of proved bounds, not inference from a sample of ambient n.

## originality

PASS

Horlemann-Ravi prove polynomiality/support decomposition for fixed diameter, and simplex extremizers are classical, but no exact all-rank a(s,k) table was identifiable from the accessible abstract and fragments; full same-paper comparison unavailable. Specialized optimal-anticode classification does not by itself enumerate all rank/support classes. Qualified O pass with priority risk explicitly retained.

## value

PASS

The finite support bound is intrinsic to bounded-weight binary linear spaces. Exact rank/support coefficients determine counts for every n and classify the extremal seven-support family, a natural complete and computationally certified invariant that can be used in coding/anticode enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
