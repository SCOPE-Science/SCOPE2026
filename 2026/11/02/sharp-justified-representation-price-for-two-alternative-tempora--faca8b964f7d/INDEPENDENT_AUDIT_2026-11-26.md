# Independent mathematical audit

## correctness

PASS

Under complete ballots and horizon L>=n, singleton JR requires every voter to be satisfied at least once, which in turn certifies JR for every group. Start from any per-round welfare maximizer, including arbitrary ties. If u voters are unsatisfied and c have satisfaction one, there are at most c critical rounds protecting the latter, so a noncritical round exists. Flipping it satisfies all u and takes no voter's last satisfaction. If a is the smallest winning approval count in a noncritical round, d=u+c and n/2<=a<=n-d. The loss is at most 2a-n and total welfare at least (L-c)a+cn/2. Their quotient increases with a. Comparing its value at n-d to (n-2)/(L(n-1)) gives a nonnegative cross-product Ln(d-1)-c(n-2)(n/2-d), strictly positive for d>1. Thus for n>=3 equality requires u=1, c=0 and a=n-1, hence every round has n-1 winner approvals. If any round's loser had more than the one unsatisfied voter's approval, flipping that round would incur strictly less than n-2 loss. This forces the fixed exclusive minority and the complementary exclusive majority in every round; direct optimization gives the converse for either choice of majority label each round. For n=2 every noncritical flip has zero loss.

## originality

PASS

The supported distinction is the sharp fixed-n, fixed-horizon welfare price on all complete time-varying binary profiles, with the one-round repair and equality iff fixed polarized minority. General complete-domain JR bounds and related static constructions are antecedents, not proof of this classification. Novelty is not credited to the JR definition or the already shared polarized examples.

## value

PASS

Restricting an agenda to two alternatives changes the welfare cost of guaranteeing every voter a satisfactory round. The sharp loss comparison quantifies that change; the repair produces a feasible nearby outcome directly from any unconstrained optimizer, while the converse identifies exactly when the worst cost cannot be avoided. This is more informative than a static example or a better constant without a mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
