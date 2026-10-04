# Singleton-gap criterion for retracts and eventual images of finite weak orders
## Finding
Let \\(W=A_1\\oplus\\cdots\\oplus A_h\\) be a finite weak order: each \\(A_i\\) is a nonempty antichain, and every point of \\(A_i\\) is below every point of \\(A_j\\) when \\(i<j\\). Let \\(Y\\subseteq W\\) be nonempty. Put
\\[
S=\\{i:Y\\cap A_i\\neq\\varnothing\\}=\\{s_1<\\cdots<s_k\\},\\qquad y_i=|Y\\cap A_i|.
\\]
Then \\(Y\\) is a retract of \\(W\\) if and only if all three conditions hold:

1. if \\(s_1>1\\), then \\(y_{{s_1}}=1\\);
2. if \\(s_k<h\\), then \\(y_{{s_k}}=1\\);
3. whenever \\(s_{{j+1}}>s_j+1\\), at least one of \\(y_{{s_j}}\\) and \\(y_{{s_{{j+1}}}}\\) equals \\(1\\).

Thus a leading or trailing block of omitted levels must meet the retained part at a singleton level, and every internal omitted block must have a singleton retained level on at least one side.

For a continuous self-map \\(f:W\\to W\\), define its eventual image by
\\[
f^{{\\infty}}(W)=\\bigcap_{{n\\geq1}} f^n(W).
\\]
The same criterion classifies exactly the subsets that can occur as \\(f^{{\\infty}}(W)\\).

## Assumptions and scope
Finite \\(T_0\\)-spaces are viewed through their specialization posets, so continuous maps are order-preserving. No lower bound on the level sizes is required; singleton levels are allowed and are exactly the gates that permit an omitted block of levels. The empty subset is excluded because no self-map of a nonempty finite space has empty image.

The statement concerns retracts as subspaces: there must exist an order-preserving map \\(r:W\\to Y\\) whose restriction to \\(Y\\) is the identity. It is distinct from the terminology “retractile set” used for a convex subset that can be collapsed to one internal point while fixing its complement.

## Proof
Assume first that \\(r:W\\to Y\\) is a retraction.

If \\(s_1>1\\), choose a point \\(x\\) in a level below \\(A_{{s_1}}\\). For every \\(z\\in Y\\cap A_{{s_1}}\\) one has \\(x<z\\), hence \\(r(x)\\leq z\\). Because \\(s_1\\) is the first retained level, \\(r(x)\\) cannot lie below \\(A_{{s_1}}\\); therefore it lies in \\(A_{{s_1}}\\). Points in one level are incomparable unless equal, so \\(r(x)\\leq z\\) for every such \\(z\\) forces all of them to equal \\(r(x)\\). Thus \\(y_{{s_1}}=1\\). The dual argument gives \\(y_{{s_k}}=1\\) when \\(s_k<h\\).

Now let \\(a=s_j\\) and \\(b=s_{{j+1}}\\) be consecutive retained levels with \\(b>a+1\\), and choose \\(x\\) in any omitted level strictly between them. For all \\(u\\in Y\\cap A_a\\) and \\(v\\in Y\\cap A_b\\),
\\[
u=r(u)\\leq r(x)\\leq r(v)=v.
\\]
There is no retained level strictly between \\(a\\) and \\(b\\), so \\(r(x)\\) lies in \\(A_a\\) or \\(A_b\\). In the first case, being above every point of \\(Y\\cap A_a\\) forces that set to be a singleton; in the second case, being below every point of \\(Y\\cap A_b\\) forces that set to be a singleton. Hence condition 3 is necessary.

Conversely assume the three conditions. Define \\(r\\) as follows. Fix every point of \\(Y\\). On a retained level \\(A_i\\), send each point of \\(A_i\\setminus Y\\) to a chosen point of \\(Y\\cap A_i\\). Send every level before \\(A_{{s_1}}\\) to the unique point of \\(Y\\cap A_{{s_1}}\\), and every level after \\(A_{{s_k}}\\) to the unique point of \\(Y\\cap A_{{s_k}}\\). For an internal omitted block between consecutive retained levels \\(A_a\\) and \\(A_b\\), send the whole block to the unique point of \\(Y\\cap A_a\\) if \\(y_a=1\\); otherwise condition 3 gives \\(y_b=1\\), and send the whole block to the unique point of \\(Y\\cap A_b\\).

Along the source levels, the target level chosen by this construction is nondecreasing. Equality of target levels across two distinct source levels occurs only when all those points are sent to the same singleton. Therefore \\(x<z\\) always implies \\(r(x)\\leq r(z)\\). Hence \\(r\\) is order-preserving and fixes \\(Y\\), so it is a retraction.

For the dynamical statement, a general finite-space result says that a subspace \\(Y\\subseteq X\\) occurs as \\(f^{{\\infty}}(X)\\) for a continuous self-map if and only if \\(Y\\) is a retract of \\(X\\). Applying that theorem to the criterion just proved gives the classification. In the reverse direction no extra existence argument is needed: the retraction constructed above is idempotent and itself satisfies \\(r^{{\\infty}}(W)=Y\\).

## Verification
The standalone script `verify_retracts.py` independently enumerates every nonempty subset and every candidate retraction for six small weak orders. It compares existence of an order-preserving retraction with the singleton-gap criterion. The verified numbers of retract subsets are \\(13,53,96,25,28,78\\) for level-size vectors \\((2,2),(2,2,2),(2,3,2),(1,2,2),(2,1,2),(1,2,3,1)\\), respectively, with no mismatches. The finite checks support the proof but are not used as an infinite argument.

## Relationship to prior work
Barmak and Minian give the standard finite-space/order correspondence used here, including that continuous maps between finite spaces are order-preserving. Barmak later proved the general dynamical equivalence \\(Y=f^{{\\infty}}(X)\\) for some self-map if and only if \\(Y\\) is a retract of the finite space \\(X\\). That theorem does not classify the retract subspaces of a weak order.

Pouzet and Zaguia describe weak orders as lexicographic sums of antichains and classify their “retractile sets.” Their term denotes a different local-collapse notion: a convex set with an internal point, used to collapse that set to one point while fixing its complement. Their criterion does not state which subsets are global retracts under maps fixing the subset pointwise. The singleton-gap theorem above supplies that missing global classification and, through the general finite-space result, an explicit classification of all eventual periodic images of weak-order self-maps.

## Limitations
The theorem uses the complete comparability between different weak-order levels. It is not claimed for arbitrary graded posets or arbitrary lexicographic sums. The literature search did not locate an earlier statement of this exact global-retract criterion, but terminology around retracts in order theory is broad; an older equivalent formulation under a different name remains a residual bibliographic risk.

## References
[1] J. A. Barmak and E. G. Minian, “Simple Homotopy Types and Finite Spaces,” arXiv:math/0611158, first submitted 2006-11-06.

[2] J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, doctoral thesis, 2008, Proposition 8.4.17.

[3] M. Pouzet and I. Zaguia, “Weak orders admitting a perpendicular linear order,” *Discrete Mathematics* 307 (2007), 97–107, doi:10.1016/j.disc.2006.05.038.
