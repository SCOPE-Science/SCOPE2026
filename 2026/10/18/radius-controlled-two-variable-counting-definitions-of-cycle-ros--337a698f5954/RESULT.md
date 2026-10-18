# Radius-controlled two-variable counting definitions of cycle roses

## Finding

For integers \(k\ge2\) and \(L_1,\ldots,L_k\ge3\), let \(R(L_1,\ldots,L_k)\) be the union of \(k\) undirected simple cycles of lengths \(L_i\), with precisely one common vertex and otherwise disjoint vertex sets. Write \(h\) for the common hub and \(D=\max_i\lfloor L_i/2\rfloor\). A counting first-order sentence using only two variables and having quantifier rank at most \(D+3\) identifies this rose among **all finite simple undirected graphs**. The complete counting-logic theory recovers the multiset of petal lengths.

There is no constant-rank version of this statement. For every \(r\ge1\), the two nonisomorphic roses
\[
A_r=R(2r+3,2r+7),\qquad B_r=R(2r+5,2r+5)
\]
have the same number \(4r+9\) of vertices and satisfy precisely the same two-variable counting sentences of rank at most \(r+1\). The largest hub-distance in \(A_r\) is \(D=r+3\), so its least possible identifying rank lies between \(D-1\) and \(D+3\), inclusive. The upper and lower bounds therefore differ by at most four on this explicit infinite family.

## Assumptions and scope

All graphs are finite, undirected, simple, without unary colours or marked constants, and are interpreted in the one-binary-predicate adjacency language. The logic \(C^2\) permits arbitrarily large numerical counting constants but only two variable names and measures the usual nesting depth of quantifiers. All \(k\ge2\), all petal lengths \(L_i\ge3\), and all finite comparison graphs are covered. The result concerns identification by sentences, not a universal sentence defining the entire class of roses.

## Proof

**Step 1: recover the hub and its distance layers.** The hub has degree \(2k\ge4\), and every other vertex has degree two. A comparison graph with the same complete counting theory therefore has precisely one vertex of degree \(2k\), all others degree two, and the same order. Degree predicates have quantifier rank one in \(C^2\). The unique-hub predicate has rank one, and inductively a formula saying that a vertex is at distance at most \(d\) from that unique hub can be built with at most two variable names and quantifier rank at most \(d+1\). Subtracting smaller balls defines each distance layer. In the given rose every vertex lies within distance \(D\) of the hub. Thus a graph agreeing on all \(C^2\) sentences of rank at most \(D+3\) also has every vertex within that distance of its hub.

**Step 2: a degree argument forces the comparison graph to be a rose.** Delete the unique high-degree hub from the comparison graph. The other vertices have induced degrees at most two, so its connected components are paths or cycles. A cycle component would be disconnected from the hub and contradict Step 1. An endpoint of a path must be adjacent to the hub because its total degree is two. An isolated component vertex would need two distinct edges to the one hub to have total degree two, impossible in a simple graph. Hence all components are paths on at least two vertices, both endpoints adjacent to the hub. Restoring the hub yields vertex-disjoint petals meeting only at it.

**Step 3: recover every petal length.** For every \(d\ge1\), among vertices at hub-distance \(d\), precisely one vertex per petal of even length \(2d\) has two neighbors at distance \(d-1\). Precisely two vertices per petal of odd length \(2d+1\) have one neighbor in the same layer. No other vertex meets either condition. These layer/neighbor-count predicates have quantifier rank at most \(d+2\) and are expressible with two variables, by alternating the variable names in the distance formulas. A top-level exact-count quantifier raises rank to at most \(d+3\). Their counts are respectively the even-petal multiplicity and twice the odd-petal multiplicity. Since \(d\le D\), the rank-\(D+3\) counting type of the rose gives every petal length multiplicity. Two roses with the same multiset of petal lengths are isomorphic.

**Step 4: a single characteristic sentence.** Canonical one-dimensional colour refinement at round \(t\) captures pointed \(C^2\)-types of quantifier rank \(t\); the histogram at round \(t\) is testable by \(C^2\) sentences of rank at most \(t+1\). For the fixed rose, conjoin exact counts of its finitely many round-\(D+2\) colour types and its total order. The conjunction has rank at most \(D+3\). The preceding three steps show that any satisfying graph is isomorphic to the rose.

**Step 5: quantitative lower bound.** Fix \(r\ge1\). The two indicated roses have two petals each, the same order, and all petal lengths at least \(2r+3\). In the first \(r\) colour-refinement rounds, a vertex sees only the degree-labelled rooted unfolding to depth \(r\). The unique degree-four hub has the same truncated unfolding in both graphs; for each distance \(d\in\{1,\ldots,r\}\), each graph has exactly four vertices at hub-distance \(d\), with the same truncated unfolding at that distance. Every remaining vertex has a truncated unfolding of the degree-two infinite path, because its distance to the hub exceeds \(r\) and no cycle closes within depth \(r\). Consequently the two graphs have identical colour histograms through round \(r\), and hence agree on all \(C^2\) sentences of quantifier rank at most \(r+1\). Their cycle-length multisets differ, so they are nonisomorphic. This proves the lower bound \(r+2=D-1\) for a characteristic sentence of \(A_r\).

## Verification

Two standalone Python-standard-library scripts accompany this result. Running `python rose_check.py` reconstructs odd/even petal multiplicities for four mixed examples and computes exact common-palette colour-refinement signatures for every \(1\le r\le30\), reproducing agreement through round \(r\) and first disagreement at round \(r+3\) for each tested pair. Running `python global_small_check.py` enumerates every labelled simple graph on five and six vertices and confirms that the roses of petal lengths \((3,3)\) and \((3,4)\) are globally distinguished at the asserted depth. These are finite corroborations only: the proof for all lengths and petal counts is Steps 1–5, not extrapolation from the experiments.

## Relationship to prior work

Kiefer, Schweitzer and Selman give a general characterization of graphs identified by \(C^2\); Arvind, Köbler, Rattan and Verbitsky give an amenability characterization. Those general classifications cover much of the underlying identification phenomenon. The claimed quantitative contribution here is the explicit hub-radius rank bound, direct petal-spectrum readout and an infinite matching-order lower-bound family within roses. Krebs and Verbitsky analyze large quantifier depths for general graphs but do not give the radius-controlled rose statement. Searches for the direct claim, flower/windmill/rose aliases, and an implication from these general theorems found no inspected prior result stating the quantitative two-sided assertion.

## Limitations

The rank upper bound is not asserted to be the exact minimum for each individual rose. The infinite lower-bound family leaves an additive gap of four, and numerical checks through \(r=30\) do not establish any sharper general formula. The result assumes a single common hub and at least two petals; arbitrary cactus graphs or edge-glued cycles are outside scope. General graph-identification theory covers the qualitative identifiability part, so originality rests on the stated explicit quantitative result. A specialized earlier quantifier-depth lemma could still imply it.

## References

1. A. Krebs and O. Verbitsky, *Universal Covers, Color Refinement, and Two-Variable Counting Logic: Lower Bounds for the Depth*, arXiv:1407.3175, first public 2014-07-11.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public 2015-02-04.
3. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first public 2015-03-30.
