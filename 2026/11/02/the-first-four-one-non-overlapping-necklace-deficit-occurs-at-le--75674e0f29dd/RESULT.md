# The first four-one non-overlapping necklace deficit occurs at length twelve

## Finding

Let \(M_4(n)\) be the maximum number of binary words of length \(n\), each of Hamming weight exactly \(4\), that can be selected so that no nonempty proper prefix of any selected word equals a suffix of any selected word, including itself. Then

\[
\begin{array}{c|rrrrrrrrr}
n&4&5&6&7&8&9&10&11&12\\\hline
M_4(n)&0&1&2&5&8&14&20&30&39.
\end{array}
\]

The primitive-necklace upper bound is sharp at every length from \(4\) through \(11\), but fails at length \(12\): there are \(40\) primitive necklaces of length \(12\) and weight \(4\), while \(M_4(12)=39\). An explicit six-necklace family has no cross-bifix-free transversal, although every five-member subfamily does have one.

## Assumptions and scope

Words are linear binary strings. A prefix or suffix is *proper* when its length is an integer \(k\) with \(1\le k<n\). For two words \(u,v\) of equal length, compatibility requires both \(u[0:k]\ne v[n-k:n]\) and \(v[0:k]\ne u[n-k:n]\) for every such \(k\). Compatibility must hold for \(u=v\) as well. A *necklace* is an orbit under cyclic rotations; a necklace is *primitive* if its orbit has exactly \(n\) distinct words. Hamming weight counts occurrences of the symbol \(1\). Only lengths \(4\le n\le12\) are asserted.

## Proof

**Rotation-class ceiling.** Every admissible codeword is unbordered, because a border is a forbidden self-overlap. Every unbordered word is primitive: a smaller period would create a nonempty proper border. Moreover, if \(u\) and \(v\) are distinct rotations of the same length-\(n\) word, say \(v=u[k:n]u[0:k]\) with \(1\le k<n\), the length-\(k\) suffix of \(v\) is the length-\(k\) prefix of \(u\). Hence a non-overlapping code contains at most one representative from each primitive necklace.

For weight \(4\), the number of primitive necklaces is

\[
P_4(n)=\frac1n\sum_{d\mid\gcd(n,4)}\mu(d)\binom{n/d}{4/d},
\]

where \(\mu\) is the Möbius function. This follows by counting primitive words through Möbius inversion and dividing by their orbit size \(n\). At lengths \(4,5,\ldots,12\), these bounds are respectively \(0,1,2,5,8,14,20,30,40\).

**Lower certificates.** `certificates.json` lists an explicit code \(C_n\) for each integer \(n\) from \(4\) through \(12\). Each listed word has weight \(4\), is unbordered, and has no prefix-suffix overlap with another listed word. The list sizes are \(0,1,2,5,8,14,20,30,39\). These facts are checked directly against the definition by `verify.py`; no optimizer is needed to verify them. For \(n\le11\) the list sizes equal \(P_4(n)\), proving all those optima.

**The length-twelve obstruction.** Consider the six distinct primitive necklaces with lexicographically least representatives

```
000010010011
000010100011
000011000101
000011001001
000100100101
000101001001
```

Each admissible representative must be an unbordered rotation of its displayed word. The numbers of such rotations are, respectively, \(3,4,4,3,3,3\). Thus exactly \(3\cdot4\cdot4\cdot3\cdot3\cdot3=1296\) candidate transversals need be examined. None has every pair compatible. This is an exhaustive finite verification: `verify.py` regenerates the rotations of each of the six displayed strings, rejects precisely the bordered ones, iterates over the Cartesian product, and directly compares both overlap orientations at all eleven proper lengths for each pair. The zero count is therefore a complete check, not a sampling argument.

Consequently a code cannot occupy all six special necklaces. There are \(40\) primitive weight-four necklaces in total, so at most five of the six and at most one of each of the remaining \(34\) can contribute. Hence \(M_4(12)\le39\), and the listed \(39\)-word code attains equality. For each of the six choices of which necklace to omit, compatible transversals of the other five exist, in respective numbers \(3,2,2,3,3,3\); thus this particular six-necklace obstruction is irredundant.

## Verification

Place `RESULT.md`, `certificates.json`, and `verify.py` in the same directory and run `python3 verify.py` using Python \(3.9\) or later. The checker uses only the standard library. It independently regenerates all binary weight-four words at each stated length, computes primitive rotation classes, validates every explicit code, checks all \(1296\) six-necklace selections, and checks the six five-necklace subfamilies. The expected terminal marker is `VERIFY_OK`. The certificate generation used discrete optimization to locate examples, but the proof and its replay do not rely on the optimizer or on an unchecked optimization log.

## Relationship to prior work

Chee, Kiah, Purkayastha, and Wang (first publicly submitted September 3, 2012) study cross-bifix-free codes, including general constructions and unrestricted binary code sizes. Blackburn (first publicly submitted March 5, 2013) studies non-overlapping codes and general size bounds, using the synonymous condition. Later work of Stanovnik, Moškon, and Mraz (2024) characterizes unrestricted maximal codes, while their 2025 study concerns polarity balance and run restrictions. The inspected statements do not give the fixed-weight-four threshold \(M_4(12)=39\) or the six-necklace obstruction. In particular, a primitive-necklace upper bound of \(40\) alone does not imply the strict deficit. This is a qualified literature comparison, not a proof of priority.

## Limitations

The exact spectrum is proved only for fixed Hamming weight \(4\) and lengths through \(12\); it does not establish any formula for larger lengths or other weights. The six-necklace obstruction is irredundant within the stated six classes, but no claim is made that six is the smallest size of an obstruction among *all* subfamilies. The finite computation is an exhaustive proof for the stated finite domain and is not an infinite-length result. Independent audit and comprehensive historical-priority certification have not been performed.

## References

1. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, first version September 3, 2012. https://arxiv.org/abs/1209.0236
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first version March 5, 2013. https://arxiv.org/abs/1303.1026
3. L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024). https://doi.org/10.1007/s10623-023-01344-z
4. L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, Computational and Applied Mathematics 44 (2025). https://doi.org/10.1007/s40314-024-03055-0
