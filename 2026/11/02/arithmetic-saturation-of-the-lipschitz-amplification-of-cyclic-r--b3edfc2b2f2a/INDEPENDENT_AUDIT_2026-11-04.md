# Independent mathematical audit

## correctness

PASS

For real n-site signals and odd cyclic windows m=2r+1<=n, all strict-order chambers have selector Jacobians J with one 1 in each row. Their exact ell_p operator norm is max_j c_j^(1/p), and continuity through order ties makes the largest chamber norm the global two-input Lipschitz constant. All m windows containing a chosen site select it iff each has exactly r below-signs. Consecutive-window comparison imposes chi_j=chi_(j+k) on sites 1..n-1 with k=n-m; the k residue chains contribute weights q or q+1 when 2r=qk+t. This establishes the iff subset-sum a(q+1)+bq=r, 0<=a<=t, 0<=b<=k-t, including n=m separately. n odd and n>=4r+1 admit explicit balancing; n=m+1 yields maximal column count r+1, and direct witness gives count 6 for (n,r)=(10,3). Infinity-norm 1 follows median monotonicity and constant translations. Independent bitmask enumeration for small r,n reproduced the multiplicities; finite tests do not prove the universal claim.

## originality

PASS

Best-of-knowledge originality qualified by primary literature, prior methods and named residual priority risks; the final evaluated theorem is not established or logically implied by the cited comparator statements.

## value

PASS

Sharp worst-case two-signal stability of a running-median smoother is a natural quantity distinct from denoising risk or signal total variation. The complete equality classification exposes arithmetic/parity obstructions and the exact short-even-cycle loss, useful for choosing window/boundary topology. A natural infinite-family exact instability threshold is neither a single toy instance nor a restatement of an evident median nonexpansivity bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
