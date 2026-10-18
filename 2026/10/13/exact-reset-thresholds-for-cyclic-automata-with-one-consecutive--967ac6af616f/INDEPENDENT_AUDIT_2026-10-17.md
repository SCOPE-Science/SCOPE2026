# Independent mathematical audit

## correctness

PASS

For n>=4, 2<=k<=n-2, b collapses exactly H=[n-k,n-1] to 0 while fixing the remaining L=n-k points; a rotates the cycle. Inverse b sends S to S∪H when 0∈S, otherwise removes H. The first productive expansion from singleton {0} leaves missing interval [1,L-1]. Every later productive inverse b removes at most k missing states. With that anchored interval, fewer than L inverse rotations either avoid H or hit 0, so cannot produce a productive b; after at least L rotations, removal leaves the same anchored-interval form. This implies >=1+t(L+1), t=ceil((L-1)/k)=floor((n-2)/k), and explicit inverse phases/reversed forward witness b(a^L b)^t attain it. Independent BFS over every reachable image subset for all 45 admitted n,k pairs through n=12 matched formula. Infinite statement follows from interval obstruction, not tests.

## originality

PASS

The full n,k reset threshold of a consecutive multi-state collapse is not determined by the referenced primitive/unimodal/semiconstant synchronizability results nor general rank bounds. Its letter has rank n-k, unlike classical single-deficiency Cerny; the exact collapse and rotation interval lower bound appears genuinely new under searched names, subject to older circular automata literature.

## value

PASS

A natural family of one-cluster cyclic automata interpolates synchronization length quadratically and linearly with collapsed-block size. Exact global shortest reset length across all words, with a sharp inverse interval obstruction, answers a core synchronization invariant and is mathematically useful beyond a small test instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
