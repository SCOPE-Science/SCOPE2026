# Independent mathematical audit

## correctness

PASS

Every weight-two n-word is an edge of the order-(n-1) de Bruijn digraph. The mandatory edges partition into cyclic rotation orbits; each touches a singleton-one (n-1)-vertex. Subtracting one mandatory traversal from any cyclic cover leaves balanced residual cycles. If fewer than n-1 residual edges exist, each residual simple cycle has period <=n-2. Fine–Wilf plus p+q<=n-2 prohibits distinct such cycles sharing a vertex; a short residual cycle meeting the adjacent-one orbit C_* cannot meet any different mandatory orbit (each of its n-1 windows contains adjacent 11, while singleton-one endpoint vertices cannot have short period). Thus the full walk cannot connect C_* to a second orbit, contradiction. Conversely the n-2 weight-one edges v_j->v_{j-1} and one duplicated 10^(n-2)1 edge create a balanced cycle through every singleton-one vertex and join every mandatory orbit; an Eulerian circuit has exactly C(n,2)+n-1 cyclic factors, with precisely the proposed multiplicities. The n>=4 boundary is required; n=2,3 differ.

## originality

PASS

Best-of-knowledge PASS for the exact shortest n-window cyclic binary covering; earlier papers define the same covering and bound it by C(n,2)+n, or construct different shorthand (n-1)-window cycles. Exact shortest formula was not found; this is not priority certification.

## value

PASS

The exact shortest cyclic superstring for the naturally defined fixed-Hamming-weight-two language resolves a tight structural covering question, improving the known constructive upper bound by one and explaining a nontrivial graph-connectivity/periodicity obstruction; it is not merely a small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
