"""Deeper verification for target p=3,k=7,j=3.
1. Confirm that MSS applies Donkin Lemma A3.1 to rule out config 1: Delta(1^10) must be a QUOTIENT of the tensor product.
2. Check the two candidate 5-factor Alperin structures: is the Donkin quotient argument alone enough to pick config 2,
   or does graded data (via alpha/gamma shifts, or ch_q) distinguish Loewy layers further?
3. Enumerate graded decomposition numbers: Lemma 3.10/Thm 3.5 forces all simples in S((ke),(je)) shifted by <j>.
   Confirm from Thm 3.5 / Cor 3.7 consequence: shifts are uniform - so graded numbers are determined up to Loewy placement.
4. General obstruction: p divides >=2 of the 2j-1 integers -> count how many Weyl modules are non-simple; show the
   Tensor product has a summand with >=5 simples where self-duality + quotient info underdetermines structure.
"""
# --- Part 1: formalize the two candidate diagrams as graphs and test self-duality + quotient condition
# Config A (MSS first): layers top->bottom? MSS picture: need to decode tikz.
# From tex: first config columns: top row L(2^2,1^6); middle row L(1^10), L(2^3,1^4), L(1^10); bottom L(2^2,1^6).
#   edges: top L22 -> all three middle; all three middle -> bottom L22.
#   That is a "diamond with doubled L(1^10)"? Actually middle has TWO copies of L(1^10)? Let's parse:
#   Row1: col2 = L(2^2,1^6). Row2: col1=L(1^10), col2=L(2^3,1^4), col3=L(1^10). Row3: col2=L(2^2,1^6).
#   Total 5 simples: L(1^10)x2, L(2^2,1^6)x2, L(2^3,1^4)x1. Matches Weyl factor content.
# Config B (MSS second): Row1: col5=L(2^2,1^6), col7=L(1^10); Row2: col6=L(2^3,1^4); Row3: col5=L(1^10), col7=L(2^2,1^6).
#   edges: 3-5 -> 1-5 (vertical left), 1-7 -> 3-7 (vertical right), 1-5 -> 2-6, 2-6 -> 3-7.
#   Hmm edges list: from=3-5 to=1-5; from=1-7 to=3-7; from=1-5 to=2-6; from=2-6 to=3-7.
#   So structure: L(1^10)(bottom-left) -- L(2^2,1^6)(top-mid); L(1^10)(top-right) -- L(2^2,1^6)(bottom-right);
#   plus chain top-mid L(2^2) -> L(2^3,1^4) -> bottom-right L(2^2).
#   Total: L(1^10)x2, L(2^2,1^6)x2, L(2^3,1^4)x1. Same content.
# Both are self-dual (symmetric). Config A has head = L(2^2,1^6) only? Actually head = top row = L(2^2,1^6).
#   Wait edges point... in Alperin diagram head at top. Config A head = L(2^2,1^6), socle = L(2^2,1^6).
#   Config B: tops are L(2^2,1^6) and L(1^10); bottoms are L(1^10) and L(2^2,1^6). Head = L(2^2) + L(1^10).
print("Content check: both configs have 2xL(1^10), 2xL(2^2,1^6), 1xL(2^3,1^4).")
print("Filtration factors: Delta(1^10)=L(1^10)[1]; Delta(2^2,1^6)=L(1^10)+L(2^2,1^6)[2]; Delta(2^3,1^4)=L(2^2,1^6)+L(2^3,1^4)[2].")
print("Total: L(1^10)x2, L(2^2,1^6)x2, L(2^3,1^4)x1. OK consistent.")
print()
print("Donkin A3.1: T = Delta(1^7)xDelta(1^3) tilting-filtered; head must contain Delta(1^10)=L(1^10) as quotient.")
print("Config A head = L(2^2,1^6) only -> L(1^10) not a quotient -> RULED OUT. Config B head contains L(1^10) -> survives.")
print("So MSS rules out config A, leaving config B as the ONLY one of the two listed. BUT:")
print("Are these the only two self-dual 5-factor modules with that Weyl filtration? Need Ext^1 data.")
print()
# --- Part 2: Ext^1 / block structure via decomposition matrix
# simples in block: L0=L(1^10), L2=L(2^2,1^6), L3=L(2^3,1^4). L1 in separate block.
# Weyl structures: D0=L0 (head=socle=L0); D2: head=L2, socle=L0 (uniserial L0|L2? or L2 on top?);
#   Standard modules have simple HEAD L(lam). So D2 = L0 | L2 (socle L0, head L2). D3 = L2 | L3.
# Self-dual summand U filtered by D0,D2,D3 with U self-dual, head contains L0 (Donkin).
# Possibilities for Loewy structure of U beyond the two drawn? Let's think via radical series constraints.
# U has top containing L0. U/D0-ish... The Weyl filtration quotients constrain submodule lattice.
# Without computing Ext^1_{S(10,10)}(L_i,L_j) one cannot enumerate all self-dual gluings.
# In particular a 5-factor self-dual module with head L0+L2 could have Loewy length 3 with middle L2+L3+L0 etc.
# MSS only asserts the two drawn are the options ('It follows that this summand has one of the following two structures').
# Is that step justified? It presumes the middle layer is forced. That is the gap to examine.
print("Gap analysis: MSS claims ONLY two possible structures for the 5-factor summand U.")
print("Justification given: self-duality + Weyl factors + block info. Is that exhaustive?")
print("U filtered by D0(head L0), D2(head L2, soc L0), D3(head L3, soc L2). U self-dual, head>>L0.")
print("Config A: head L2. Config B: head L0+L2 with socle L0+L2 (a 'parallelogram').")
print("But e.g. a uniserial L2|L3|L0|L2|L0? No - must be self-dual, so uniserial of odd length with symmetric factors.")
print("Possible uniserial symmetric with content {0x2,2x2,3x1}: middle must be L3 (unique), pairs symmetric: L0|L2|L3|L2|L0 or L2|L0|L3|L0|L2.")
print("First = N_1-like stacking; second = reverse. Config A is NOT uniserial (middle layer has 3 factors).")
print("So uniserial options exist in principle; MSS excludes them silently. Need Ext vanishing to exclude.")
print("Hence the 'one of two structures' claim itself needs Ext^1 computation - the target asks to DECIDE.")
