# Independent mathematical audit

## correctness

PASS

For each m>=1 the first/last differing positions in equal-length palindromes are symmetric. Common one-deletion descendants force their centered differing interval to alternate with complementary phases, and deleting its opposite endpoints proves the converse. Even-length centers contain equal symbols so no nontrivial alternating interval exists. For odd length 2m-1 the halfword edge criterion is exactly a complementary alternating tail. Recursive separation by first bit produces two rooted copies joined by their alternating-root edge, a binomial tree with 2^m vertices. A last-bit perfect matching bounds independence by 2^(m-1); tree bipartition attains it. Rooted maximum-independent-set recurrence N_m=N_(m-1)^2-A_(m-1)^2, A_m=A_(m-1)(N_(m-1)-A_(m-1)), with N_1=2,A_1=1 yields N_m=(m+1)prod_{j=1}^{m-1}j^{2^(m-1-j)}. Independently constructed deletion shadows and alternating-tail predicted graph for m=1..6: every odd edge agrees; even graphs empty. Finite m checks corroborate the all-m proof.

## originality

PASS

The abstract binomial-tree maximum independent-set product is already in OEIS A347289 and is not separately original. The nontrivial original assertion under best-of-knowledge comparison is the explicit isomorphism from one-deletion-confusability of binary palindromic words and the exact even/odd coding-optima interpretation, absent from the inspected unrestricted deletion-code literature.

## value

PASS

Binary palindromic codewords are a natural constrained family under synchronization errors. The exact infinite confusability graph isomorphism, parity dichotomy in capacity and exact labeled optimizer count give genuinely motivated structural data, beyond an arbitrary low-length computation. This does not assert efficiency for unrestricted deletion codes or DNA applicability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
