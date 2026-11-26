# Independent mathematical audit

## correctness

PASS

Marking one occurrence of every linear-one-run window leaves an integral flow from N_i = 1^i0^(k-1-i) to P_j = 0^(k-1-j)1^j in the full de Bruijn digraph. Each path must shift away i leading ones before it can reach any P_j. At equality there are no surplus cycles and the arrival after i steps forces j <= i. Bijectivity forces j=i, hence the appended symbols are forced to be 1^i. This proves both the unrestricted lower bound and the forced exact circular-one-run spectrum. The mandatory subgraph is strongly connected via 0^(k-1); adding the paths balances it and attaches every new vertex. For the enumeration, the BEST formula applies with the unique 0^k loop fixed first. In an in-tree toward 0^(k-1), the largest N_i that would select its path to P_i would return to itself, via some N_j with j>=i whose larger indices all descend, so all N_i must descend. The k-2 P_i each have two independent choices. The empty-flow and empty-choice cases at k=2 yield one class. An independently constructed out-Laplacian cofactor, taking windows with at most two circular changes, gave determinants 1,2,4,8,16,32,64,128,256 for k=2..10; this is finite corroboration, not the all-k proof.

## originality

PASS

Pass for the combined optimal-cover result, particularly the unrestricted lower bound and mandatory forced completion. The standalone existence and rotation count for universal cycles of the completed family are demonstrably covered in another published Resultary statement. This overlap is credited explicitly, not treated as a separately distinct result or used to infer priority from dates.

## value

PASS

This is a natural family for cyclic coverage. Proving a sharp overhead against all binary hosts, even those allowed to use arbitrary extra windows, and identifying every extra window at equality is substantially more informative than constructing one universal cycle. It also tells a user precisely when the completed-family enumeration counts all optimal hosts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
