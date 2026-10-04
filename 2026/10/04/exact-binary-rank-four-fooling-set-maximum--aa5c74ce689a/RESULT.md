# Exact binary rank-four fooling-set maximum

## Finding
Let \(\mathbb F_2\) be the binary field. A square matrix \(M\in\mathbb F_2^{n\times n}\) is a fooling-set matrix when \(M_{ii}\ne0\) for every \(i\) and \(M_{ij}M_{ji}=0\) for every distinct \(i,j\). Write \(f_{\mathbb F_2}(r)\) for the largest order of a fooling-set matrix over \(\mathbb F_2\) having rank at most \(r\). Then
\[
f_{\mathbb F_2}(4)=11.
\]

## Assumptions and scope
The field is exactly \(\mathbb F_2\), and rank is ordinary matrix rank over that field. The claim concerns arbitrary square fooling-set matrices, not only symmetric, circulant, Toeplitz, or Boolean matrices arising from a fixed communication problem. Since every matrix over \(\mathbb F_2\) is binary, no separate zero-nonzero weighting issue occurs.

## Proof
For the lower bound, the following matrix is a fooling-set matrix of rank four over \(\mathbb F_2\):

```text
10111100001
11010101100
01111000110
00010001011
01011111000
00110110101
11110010010
00100111110
10001010100
11000100111
01101001101
```

Exact Gaussian elimination over \(\mathbb F_2\) gives rank four, every diagonal entry is one, and for every distinct pair \(i,j\), at least one of \(M_{ij},M_{ji}\) is zero. Hence \(f_{\mathbb F_2}(4)\ge11\).

For the upper bound, let \(M\) be any fooling-set matrix of rank at most four. A rank factorization gives \(M=UV^{T}\) with rows \(u_i,v_i\in\mathbb F_2^4\). Because \(M_{ii}=1\), each index \(i\) determines an ordered pair \((u_i,v_i)\) satisfying \(u_i\cdot v_i=1\). There are exactly \(15\cdot8=120\) such ordered pairs.

Define a graph \(G\) on these 120 pairs. Distinct vertices \((u,v)\) and \((u',v')\) are adjacent exactly when they are compatible with the fooling-set condition, namely when it is not the case that both \(u\cdot v'=1\) and \(u'\cdot v=1\). Repeated pair-types are impossible in a fooling-set matrix because repetition would make both opposite cross entries one. Therefore the indices of any rank-at-most-four binary fooling-set matrix form a clique in \(G\). Conversely, every clique in \(G\) gives such a matrix by taking the corresponding dot products. Thus \(f_{\mathbb F_2}(4)=\omega(G)\).

The standalone verifier enumerates all 120 vertices and all compatibility edges, then computes \(\omega(G)\) by an exact branch-and-bound maximum-clique search. Each recursive node is bounded by a greedy proper coloring of the remaining induced graph; the color count is a rigorous clique upper bound. The exhaustive search returns \(\omega(G)=11\). Combined with the displayed witness, this proves the equality.

## Verification
Running `python3 artifacts/verify_rank4_f2.py` prints `VERIFY_OK`. The verifier independently checks the displayed witness, its exact \(\mathbb F_2\)-rank, the 120-type reduction, and the exhaustive maximum-clique computation. The recorded run examines 12,096 branch nodes and obtains exact maximum clique size 11. No floating-point optimization or external solver is used.

## Relationship to prior work
Dietzfelbinger, Hromkovič, and Schnitger proved the general bound \(n\le \operatorname{rank}(M)^2\), which gives only 16 at rank four. Friesen, Hamed, Lee, and Theis constructed asymptotically quadratic fooling-set families in positive characteristic; their finite-field construction specializes to ranks \(r=2^t+1\) over \(\mathbb F_2\), so it does not determine rank four. Hamed and Lee constructed size \(\binom{r+1}{2}\) at rank \(r\) in characteristic zero, giving the nearby generic size ten at rank four rather than the binary optimum.

A published rank-three result determines \(f_{\mathbb F_2}(3)=7\) and gives the general tournament bound \(f_{\mathbb F}(r)\le2^r-1\); at rank four this yields only 15. Targeted searches under fooling-set matrices, Hadamard factorizations of the identity, cross-free matchings, and low-rank binary formulations did not identify a prior exact value for \(f_{\mathbb F_2}(4)\). The present claim is therefore made to the best of current bibliographic knowledge.

## Limitations
The upper bound is a finite exhaustive computation on a rigorously derived 120-vertex graph rather than a short structural classification. The result is specific to \(\mathbb F_2\); it does not determine rank four over larger finite fields or characteristic zero. Bibliographic searches cannot rule out an unindexed equivalent statement under minimum-rank or sign-pattern terminology, so the originality conclusion retains that residual risk.

## References
1. M. Dietzfelbinger, J. Hromkovič, and G. Schnitger, “A comparison of two lower-bound methods for communication complexity,” *Theoretical Computer Science* 168 (1996), 39–51. DOI: 10.1016/S0304-3975(96)00062-X.
2. M. Friesen, A. Hamed, T. Lee, and D. O. Theis, “Fooling-sets and rank,” *European Journal of Combinatorics* 48 (2015), 143–153. DOI: 10.1016/j.ejc.2015.02.016; arXiv:1208.2920.
3. A. Hamed and T. Lee, “Rank and fooling set size,” arXiv:1310.7321 (2013).
4. “Exact maximum size of rank-three fooling-set matrices,” published record `2026/9/21/SCOPE-rank-three-fooling-set-matrices--5e979acb344b`.
