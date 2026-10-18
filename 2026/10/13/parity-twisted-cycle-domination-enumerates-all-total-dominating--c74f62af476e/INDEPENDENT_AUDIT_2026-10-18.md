# Independent mathematical audit

## correctness

PASS

For Y_n=C_n square K2, total domination is Boolean x_{i-1,r}∨x_{i+1,r}∨x_{i,1-r}. When n odd, CRT bijection j mod2n ↔ (j mod n,j mod2) transforms all conditions into no cyclic 000 triple of length 2n, exactly ordinary C_{2n} domination. When n even, the two classes y_i^(s)=x_{i,(i+s) mod2} partition all positions into two independent length-n cyclic words, each avoiding 000. Both maps preserve selected-vertex number, giving T_n=D_{2n} odd or D_n² even for all n>=3. Cyclic run-gap lengths 1,2,3 yield D_m coefficient m(k−1)!/(a!b!c!) with a+2b+3c=m. The transfer log-det identity follows from the 16-state weighted transition matrix and formal trace determinant; inspected the exact verifier implementation. Independent brute enumeration of all 2^(2n) subsets for n=3..7 matched the complete polynomial (totals 39,121,443,1521,5071); this is corroboration, not the all-n proof.

## originality

PASS

Azarija–Henning–Klavžar, arXiv:1606.08143, establish minimum total-domination equality for bipartite prism graphs and study odd cycle prisms; their proof anticipates even splitting but does not give coefficientwise T_n(z)=D_n(z)^2 or the odd n degree-doubling T_n=D_{2n}. Hu et al. arXiv:1607.00400 establish polynomial recursions for cycles and paths but not a prism factorization. OEIS A296102/A303053/A302405 tabulate scalar totals/minima; those scalars do not determine every coefficient. The odd-parity exact bijection and uniform complete size enumerator survive.

## value

PASS

Total domination is a natural network coverage invariant, and a full cardinality polynomial controls all set sizes and independent-site-selection reliability, unlike minimum or ungraded totals. The odd/even parity structure is an exact, surprising double-length cycle versus independent-cycle square reduction with reusable weight-preserving bijections, not a tiny computed sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
